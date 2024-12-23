from fastapi import FastAPI, HTTPException
from utils import fetch_tasks, add_task, retrieve_task_from_db,db
from models import TaskInput, Task
from ai_utils import generate_category, generate_summary
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    return "Hello, How are you? I'm under the water!"

@app.get("/tasks")
async def fetch_data():
    return fetch_tasks()

@app.post("/tasks")
async def create_task(task_input: TaskInput):
    try:
        category = generate_category(task_input.title, task_input.description)
        time= datetime.now()
        task = Task(**task_input.model_dump(), category=category,created_at=time)
        task_id = add_task(task)
        return {"message": "Task added successfully", "task_id": task_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to add task: {str(e)}")
    
@app.get("/tasks/{id}")
async def get_task(id: str):
    try:
        task = retrieve_task_from_db(id)
        return task
    except ValueError as e:
        raise HTTPException(status_code=404, detail=f"No such task of this id. {str(e)}")
    
@app.post("/task/{id}/summarize")
async def summarize(id: str):
    try:
        task=retrieve_task_from_db(id)
        description = task.get('description')
        summary=generate_summary(description)
        db.collection("tasks").document(id).update({"summary": summary})
        return {"message": "Summary successfully added to the task.", "summary": summary}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"No description on this task given. {str(e)}")