
import asyncio
import sqlite3
from pathlib import Path

from maintenance.controller import BACKUP_DIR, PROJECT_DIR


async def restore_backup(backup_filename):
    """Restore a backup into a separate test database."""

    backup_path = BACKUP_DIR / backup_filename
    restored_path = PROJECT_DIR / "meals_restored.db"

    if not backup_path.is_file():
        raise FileNotFoundError("Backup file not found")

    if backup_path.suffix != ".db":
        raise ValueError("Invalid backup file")

    def restore():
        # Copy database contents using SQLite's backup API
        with sqlite3.connect(backup_path) as source:
            with sqlite3.connect(restored_path) as destination:
                source.backup(destination)

        # Verify the restored recipes
        with sqlite3.connect(restored_path) as connection:
            result = connection.execute(
                "SELECT COUNT(*) FROM recipes"
            )
            return result.fetchone()[0]

    count = await asyncio.to_thread(restore)

    return {
        "status": "restored",
        "database": str(restored_path),
        "recipes": count
    }
