from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

# class User(BaseModel):
#     name: str
#     age: int
#     email: str

#multiple routes
#@app.get("/")
#def home():
#    return {"message": "Hello Without vern"}

#@app.get("/about")
#def about():
#    return {"message": "This is the about page"}

#@app.get("/users")
#def users():
#    return {
#        "users":["Mohit","Rohit","Shivam"]
#    }

#dynamic routing

#@app.get("/users/{user_id}")
#def get_user(user_id: int):
#    return {"user_id": user_id}

# @app.get("/users")
# def get_users(name: str):
#     return{"Name": name}

# @app.get("/products")
# def get_products(limit: int = 10):
#     return{"limit": limit}

# @app.get("/items")
# def get_items(name: str = None, price: int = 0):
#     return{"name": name, "price": price}

# @app.post("/create-user")
# def create_User(User:dict):
#     return {"message": "User created successfully","data": User}

#CRUD Operations

todos=[]

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {"message": "Todo created successfully","data": todo}

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error": "Todo not found"}


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {"message": "Todo updated successfully","data": updated_todo}
    return {"error": "Todo not found"}


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted successfully"}
    return {"error": "Todo not found"}
