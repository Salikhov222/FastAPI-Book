from typing import Optional, List

from pydantic import BaseModel, EmailStr
from beanie import Document, Link
from models.events import Event

class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]] = None

    class Settings:
        name = "users"

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": []
            }
        }

class TokenResponse(BaseModel):
    access_token: str
    token_type: str