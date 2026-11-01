
import pytest
from unittest.mock import AsyncMock

from maintenance.controller import MaintenanceController


@pytest.mark.asyncio
async def test_healthy_database():
    controller = MaintenanceController()
    controller.check_database = AsyncMock(return_value=True)

    result = await controller.run_maintenance()

    assert result["status"] == "healthy"


@pytest.mark.asyncio
async def test_unhealthy_database():
    controller = MaintenanceController()
    controller.check_database = AsyncMock(return_value=False)

    result = await controller.run_maintenance()

    assert result["status"] == "unhealthy"


@pytest.mark.asyncio
async def test_database_check():
    controller = MaintenanceController()

    result = await controller.check_database()

    assert result is True
