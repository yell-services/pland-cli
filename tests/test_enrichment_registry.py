import click
from click.testing import CliRunner

from pland_cli.enrichment.registry import _REGISTRY, OVERRIDES, apply_enrichment, enrich


def test_enrich_replaces_generated_command():
    _REGISTRY.clear()
    OVERRIDES.clear()

    @enrich("demo", "list")
    @click.command()
    def custom_list():
        click.echo("ENRICHED")

    group = click.Group("demo")
    @group.command("list")
    def _gen():
        click.echo("GENERATED")

    apply_enrichment("demo", group)
    result = CliRunner().invoke(group, ["list"])
    assert "ENRICHED" in result.output
    assert ("demo", "list", False) in OVERRIDES


def test_enrich_new_adds_command():
    _REGISTRY.clear()
    OVERRIDES.clear()

    @enrich("demo", "report", new=True)
    @click.command()
    def report():
        click.echo("NEW")

    group = click.Group("demo")
    apply_enrichment("demo", group)
    result = CliRunner().invoke(group, ["report"])
    assert "NEW" in result.output
    assert ("demo", "report", True) in OVERRIDES


def test_apply_enrichment_marks_short_help():
    _REGISTRY.clear()
    OVERRIDES.clear()

    @enrich("demo", "report", new=True)
    @click.command()
    def report():
        """Tut etwas Nützliches."""

    group = click.Group("demo")
    apply_enrichment("demo", group)
    assert group.commands["report"].short_help == "(enriched) Tut etwas Nützliches."


def test_mark_enriched_is_idempotent():
    _REGISTRY.clear()
    OVERRIDES.clear()

    @enrich("demo", "report", new=True)
    @click.command()
    def report():
        """Tut etwas."""

    group = click.Group("demo")
    apply_enrichment("demo", group)
    apply_enrichment("demo", group)  # zweiter Lauf darf nicht doppelt markieren
    assert group.commands["report"].short_help == "(enriched) Tut etwas."


def test_real_salary_group_marks_only_enriched():
    from pland_cli.cli import main

    salary = main.commands["salary"]
    for name in ("for-object", "monthly-report"):
        assert salary.commands[name].short_help.startswith("(enriched)")
    # Generierte Commands bleiben unmarkiert.
    for name in ("get", "list-salaries"):
        sh = salary.commands[name].short_help
        assert sh is None or "(enriched)" not in sh
    help_out = CliRunner().invoke(main, ["salary", "--help"]).output
    assert "(enriched)" in help_out
