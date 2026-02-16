from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Data model (like TypeScript interface)
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    completed: bool = False

# In-memory storage
tasks = []
next_id = 1

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    global next_id
    task.id = next_id
    next_id += 1
    tasks.append(task)
    return task

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    return {"error": "Task not found"}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    # Find the task in the list
    for i, t in enumerate(tasks):
        if t.id == task_id:
            # Update it
            task.id = task_id  # Keep the same ID
            tasks[i] = task
            return task

    # If not found
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t.id != task_id]
    return {"message": "Task deleted"}