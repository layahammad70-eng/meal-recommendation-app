
import asyncio
import sqlite3
from datetime import datetime
from pathlib import Path

from sqlalchemy import text
from backend.database import engine


# Project folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATABASE_FILE = PROJECT_DIR / "meals.db"
BACKUP_DIR = PROJECT_DIR / "backups"


class MaintenanceController:

    async def check_database(self):
        """Check whether the database responds."""

        def check():
            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))

        try:
            await asyncio.to_thread(check)
            return True
        except Exception:
            return False

    async def create_backup(self):
        """Create a consistent SQLite database backup."""

        if not DATABASE_FILE.exists():
            return None

        BACKUP_DIR.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S_%f"
        )

        backup_file = BACKUP_DIR / f"meals_{timestamp}.db"

        def backup_database():
            with sqlite3.connect(DATABASE_FILE) as source:
                with sqlite3.connect(backup_file) as destination:
                    source.backup(destination)

        await asyncio.to_thread(backup_database)

        return str(backup_file)

    async def run_maintenance(self):
        """Check database health and report status."""

        healthy = await self.check_database()

        if healthy:
            return {
                "status": "healthy",
                "message": "Database is working."
            }

        return {
            "status": "unhealthy",
            "message": "Database connection failed."
        }


async def main():
    controller = MaintenanceController()

    result = await controller.run_maintenance()
    print(result)

    if result["status"] == "healthy":
        backup = await controller.create_backup()
        print("Backup:", backup)


if __name__ == "__main__":
    asyncio.run(main())
