# Ref: https://www.gormanalysis.com/blog/building-a-simple-crud-application-with-fastapi/
from fastapi import FastAPI, status
from database import Base, engine

# Create a database
Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello world"}

@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo():
    pass

@app.get("/get/{id}")
def redo_todo(id: int):
    return f"read todo item with id {id}"


@app.put("/todo/{id}")
def update_todo(id: int):
    return f"update todo item with id {id}"

@app.delete("/todo/{id}")
def delete_todo(id: int):
    return f"delete todo item with id {id}"

@app.get("/todo")
def read_todo_list():
    return "read todo list"
