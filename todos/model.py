# Pydantic - библиотека для проверки (валидации) данных с помощью аннотаций
from typing import List, Optional

from fastapi import Form
from pydantic import BaseModel


class Todo(BaseModel):
    id: Optional[int] = None   # Optinal[...] = Union[..., None]
    item: str

    # Метод класса, cls - аргумент, который представляет сам класс
    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(item=item)

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