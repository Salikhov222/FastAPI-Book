from typing import Optional, Any, List

import asyncio

from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import  BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from models.events import Event
from models.users import User


class Settings(BaseSettings):
    SECRET_KEY: Optional[str] = None
    DATABASE_URL: Optional[str] = None
    
    model_config = SettingsConfigDict(env_file='.env')

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        # Рабочий цикл и цикл motor одинаковый
        client.get_io_loop = asyncio.get_running_loop 
        await init_beanie(
            database=client.get_default_database(), document_models=[Event, User],
        )


class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()
        return
    
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False
    
    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs
    
    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.model_dump()    # Преобразование в словарь (сериализация)
        des_body = {k:v for k,v in des_body.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}

        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc
    
    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True
    


