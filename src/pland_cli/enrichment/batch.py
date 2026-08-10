"""Run many spec operations from one file behind a single risk gate."""
from __future__ import annotations

RISK_ORDER = {"free": 0, "confirm": 1, "critical": 2}


def max_risk(risks: list[str]) -> str:
    """Highest risk level in the list; "free" for an empty list."""
    highest = "free"
    for risk in risks:
        if risk not in RISK_ORDER:
            raise ValueError(f"unknown risk level: {risk!r}")
        if RISK_ORDER[risk] > RISK_ORDER[highest]:
            highest = risk
    return highest
