from pydantic import BaseModel


class CreateTodoRequest(BaseModel):
    todo_detail: str


class UpdateTodoRequest(BaseModel):
    todo_id: int
    new_todo_detail: str
