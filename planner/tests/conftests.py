import asyncio
import httpx
import pytest

from main import app
from database.connection import Settings
from models.events import Event
from models.users import User


# Фикстура сеанса цикла
@pytest.fixture(scope="session", autouse=True)
async def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


async def init_db():
    test_settings = Settings()
    test_settings.DATABASE_URL = "mongodb://localhost:27017/testdb"

    await test_settings.initialize_database()


# Фикстура возвращает экземпляр приложения, работающего асинхронно через httpx
@pytest.fixture(scope="session")
async def default_client():
    await init_db()
    async with httpx.AsyncClient(app=app, base_url="http://app") as client:
        yield client
        
        # Clean up resourses
        await Event.find_all().delete()
        await User.find_all().delete()
        