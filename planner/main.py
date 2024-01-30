import uvicorn
from functools import lru_cache

from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse

from database.connection import Settings
from routes.users import user_router
from routes.events import event_router


# Создание объекта Settings один раз при его первом вызове
@lru_cache
def get_settings():
    return Settings()

# Функция с асинхронным менеджером контекста, которая выполняется перед тем, как приложение начнет получать запросы
@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    await settings.initialize_database()
    yield


app = FastAPI(lifespan=lifespan)


# Register routes
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)