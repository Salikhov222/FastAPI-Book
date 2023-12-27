# Pydantic - библиотека для проверки (валидации) данных с помощью аннотаций

from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: int
    item: str

    # класс для указания примера заполнения данных в модели
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "Example_schema"
            }
        }

class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Condig:
        json_schema_extra = {
            "exmaple": {
                "todos": [
                    {
                        "item": "Example schema 1"
                    },
                    {
                        "item": "Example schema 2"
                    }
                ]
            }
        }