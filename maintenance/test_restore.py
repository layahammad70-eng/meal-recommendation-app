
import asyncio

from maintenance.controller import BACKUP_DIR
from maintenance.restore import restore_backup


async def main():
    # Find available backups
    backups = sorted(BACKUP_DIR.glob("meals_*.db"))

    if not backups:
        print("No backups found.")
        return

    # Use the latest backup
    latest_backup = backups[-1]

    print("Restoring:", latest_backup.name)

    # Restore to a separate database
    result = await restore_backup(latest_backup.name)

    print("Status:", result["status"])
    print("Database:", result["database"])
    print("Recipes restored:", result["recipes"])


if __name__ == "__main__":
    asyncio.run(main())
