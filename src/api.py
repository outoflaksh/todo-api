from fastapi import FastAPI
from .db import fetch_all_tasks, create_task, complete_task, update_task, delete_task
from .models import CreateTodoRequest, UpdateTodoRequest

app = FastAPI()


@app.get("/")
def read_index():
    return {"msg": "This is the index page!"}


@app.get("/todo")
def read_all_todos():
    todo_list = fetch_all_tasks()

    return {
        "success": True,
        "data": todo_list,
    }


@app.post("/todo")
def create_a_todo(todo: CreateTodoRequest):
    create_task(**dict(todo))

    return {
        "success": True,
    }


@app.put("/complete-todo")
def complete_a_todo(todo_id: int):
    complete_task(todo_id)

    return {
        "success": True,
    }


@app.put("/todo")
def update_a_todo(new_todo: UpdateTodoRequest):
    update_task(**dict(new_todo))

    return {
        "success": True,
    }


@app.delete("/todo")
def delete_a_todo(todo_id: int):
    delete_task(todo_id)

    return {
        "success": True,
    }
