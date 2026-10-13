"""Typer CLI surface for the desktop tool.

Commands map 1:1 to pipeline stages so power users can run pieces
individually: ``ingest``, ``run``, ``export``, ``inspect``.
"""
from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from src.bootstrap import bootstrap
from src.ingest.file_handler import ingest_file
from src.jobs.job import Job

app = typer.Typer(add_completion=False, help="AI physics simulation generator (desktop).")
console = Console()


@app.command()
def version() -> None:
    """Print version and exit."""
    from src import __version__

    console.print(f"ai-physics-sim-generator {__version__}")


@app.command()
def run(
    spec: Path = typer.Argument(..., exists=True, readable=True),
    driver: str = typer.Option("apsim_bundle", "--driver", "-d"),
    out: Path | None = typer.Option(None, "--out", "-o"),
) -> None:
    """Ingest a spec and run it end to end through the pipeline."""
    pipeline = bootstrap()
    sim_spec = ingest_file(spec)
    job = Job(spec=sim_spec, driver_name=driver, output_dir=out)
    result = pipeline.run(job)
    console.print(f"[green]ok[/] job={result.job_id} steps={result.steps} artifact={result.artifact}")


@app.command()
def inspect(spec: Path = typer.Argument(..., exists=True, readable=True)) -> None:
    """Parse a spec and print its normalized form."""
    sim_spec = ingest_file(spec)
    table = Table(title=f"SimSpec: {sim_spec.name}")
    table.add_column("field")
    table.add_column("value")
    for key, value in sim_spec.summary().items():
        table.add_row(key, str(value))
    console.print(table)


if __name__ == "__main__":
    app()