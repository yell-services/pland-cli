"""Build-Zeit-Klassifizierung schreibender Operationen in Risiko-Stufen.

Stufen: "free" | "confirm" | "critical". Die Logik ist deterministisch aus
(method, path, tag) abgeleitet — Heuristik + kuratierte Tag-Mengen. Siehe
docs/superpowers/specs/2026-06-01-pland-cli-destructive-guard-design.md.
"""
from __future__ import annotations

# Stammdaten/Konfiguration: delete/update gilt als unkritisch (leicht neu anlegbar)
CONFIG_TAGS = {
    "Activity Types", "Equipment Types", "Task Types", "Tax Rates",
    "Payment Methods", "Payment Terms", "Service Products", "Holiday",
    "Surcharges", "Invoice Templates", "Invoice Reminder Templates", "Articles",
}
# Ressourcen mit Entwurf-Zustand: DELETE ist zustandsabhaengig (Entwurf -> frei)
DRAFTABLE_TAGS = {"Invoice", "Credit", "Offers", "Invoice Storno"}

_READISH = (
    "/preview", "/pdf", "/zip", "/export", "/dashboard", "/overview",
    "capacities", "calculate", "loadcalendar", "loadresources",
    "nextinvoicedatepreview", "getsalarygroups", "checkcapacity",
    "usercapacities", "jobsintimeframe", "letterprice", "/exportsalaryrows",
    "objectexport",
)


def classify(method: str, path: str, tag: str) -> str:
    m = method.lower()
    p = path.lower()
    last = p.rstrip("/").split("/")[-1]

    # 1) Semantisch lesend trotz POST -> free
    if m == "post" and any(k in p for k in _READISH):
        return "free"
    if any(p.endswith(x) for x in ("/preview", "/pdf", "/zip", "/export", "/dashboard")):
        return "free"

    # 2) Notifications: Massenloeschung kritisch, Marker frei
    if "notification" in p:
        if "deleteall" in p or last == "delete":
            return "critical"
        return "free"

    # 3) Triviale Marker / Session-Token -> free
    if any(k in p for k in ("markmessagesasread", "lasttimeactive", "setdevicetoken",
                            "webpushtoken", "clickedlink", "/callback", "/started")):
        return "free"
    if p.endswith("/chat"):
        return "free"

    # 4) Account-Sicherheit -> critical
    if "change-password" in p or "generatepassword" in p or "sendsmstoallusers" in p:
        return "critical"
    if p.startswith("/api_key/") and m in ("delete", "patch"):
        return "critical"

    # 5) Cascade-Enddatum -> critical
    if "setenddate" in p and "andall" in p:
        return "critical"

    # 6) Lohn/Gehalt -> critical
    if tag == "Salary" and (m in ("delete", "patch") or "release" in p):
        return "critical"

    # 7) Zeiterfassung: Freigaben/Storno -> critical; operativ -> free
    if tag == "Time Tracking":
        if any(k in p for k in ("/cancel", "/customtime", "/targettime",
                                "/workingtime", "/uncancel")):
            return "critical"
        return "free"

    # 8) Massen-Schreibvorgaenge
    if last == "delete":
        return "critical"
    if last == "many":
        return "confirm"

    # 9) Users delete + Invoices Massen-Storno
    if tag == "Users" and m == "delete":
        return "critical"
    if p == "/invoices/settocanceled":
        return "critical"

    # 9b) Dokumente: Loeschen/Aendern -> critical (kein --yes-Bypass). Ein realer
    # Agent-Test zeigte, dass die confirm-Stufe per --yes umgangen wird; Dokumente
    # (Lohn-/SV-Abrechnungen u.a.) brauchen den harten, nur-Mensch-Schutz.
    # Hochladen/Hinzufuegen (POST/upload) bleibt bewusst frei (additiv, harmlos).
    if tag == "Documents" and m in ("delete", "patch"):
        return "critical"

    # 10) Self-Service-Auth (login/forgot/sms) -> free (change-password ist oben kritisch)
    if tag == "Authentication":
        return "free"

    # 11) Konfiguration/Stammdaten -> free (Pay Types ist NICHT enthalten -> faellt zu confirm)
    if tag in CONFIG_TAGS and m in ("delete", "patch", "put"):
        return "free"

    # 12) Logbuch-Chat-Nachrichten -> free
    if tag == "Logbuch":
        return "free"

    # 13) Externer Versand -> confirm
    if any(k in p for k in ("/send", "sendletter", "sendsms", "sendxrechnung",
                            "sendzugferd")) or last.startswith("send"):
        return "confirm"

    # 14) Create (POST auf Ressourcen-Root o. Standard-Aktionen) -> free
    if m == "post" and (p.endswith("/") or last in (
            "v2", "withassignment", "withurl", "import", "duplicate", "absence", "salary")):
        return "free"

    # 15) Status-Finalisierung -> confirm
    if any(k in p for k in ("setfixed", "settofixed", "setto", "finishorder",
                            "/resolve", "/complete", "/approve", "/decline",
                            "/cancel", "setmultiple", "/match", "/unmatch",
                            "/ignore", "/sign", "setfaktured", "tofaktured")):
        return "confirm"

    # 16/17) DELETE/UPDATE echter Geschaeftsdaten -> confirm
    if m in ("delete", "patch", "put"):
        return "confirm"

    # 18) Rest-POST: additive Sub-Aktionen -> free, sonst confirm (fail-safe)
    if m == "post":
        if last in ("location", "profileimage", "companylogo", "members",
                    "removemembers", "subscribe", "unsubscribe", "addmaterial",
                    "material", "adddocuments", "attachdocuments", "upload",
                    "uploaddocuments", "consenttobankintegration", "filter",
                    "createchannel", "sendnote", "sendthread", "pin"):
            return "free"
        return "confirm"

    return "confirm"


def draftable_for(method: str, path: str, tag: str) -> str | None:
    """Tag-Key fuer den Entwurf-Lookup, falls dies ein DELETE auf eine
    draftfaehige Ressource ist; sonst None."""
    if method.lower() == "delete" and tag in DRAFTABLE_TAGS and path.rstrip("/").endswith("}"):
        return tag
    return None
