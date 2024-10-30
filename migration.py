from typing import Any, Required
import typer
import os
import subprocess
from contextlib import chdir

app = typer.Typer(no_args_is_help=True, add_completion=False)


@app.command(name="new-migration", short_help="Create a new migration in alembic")
def newMigration(
    migration_name: Any = typer.Option(help="Name for this migration")
) -> None:
    with chdir(os.path.join("bot","utils","database")):
        subprocess.call(["ls", "-al"])
        subprocess.call(["alembic", "revision", "--autogenerate", "-m", f'"{migration_name}"'])


if __name__ == "__main__":
    app()
