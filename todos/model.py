# Pydantic - библиотека для проверки (валидации) данных с помощью аннотаций

from pydantic import BaseModel

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