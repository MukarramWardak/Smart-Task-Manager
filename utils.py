import firebase_admin
from firebase_admin import credentials, firestore
from models import TaskInput

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

task_ref=db.collection('tasks')


def fetch_tasks():
    task_list=[]
    docs=task_ref.stream()
    for doc in docs:
        task_list.append(f"Task ID : {doc.id} -- Task {doc.to_dict()}")
    return task_list

def add_task(task_input:TaskInput):
    new_task=task_ref.add(task_input.model_dump())
    return new_task[1].id

def retrieve_task_from_db(id: str):
    doc_ref = db.collection("tasks").document(id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        raise ValueError("Task not found")