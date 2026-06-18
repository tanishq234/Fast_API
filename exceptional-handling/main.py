from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

#custom exception-use multiple time code

class UserNotFoundException(Exception):
    def __init__(self,name:str):
        self.name = name

#global error handling
@app.exception_handler(UserNotFoundException)
def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"status": "Error", "message": f"User '{exc.name}' not found"}
    )

@app.get("/user/{name}")
def get_user(name: str):
    if name != "John Doe":
        raise UserNotFoundException(name)
    return {"name": name}

# @app.get("/user/{user_id}")
# def get_user(user_id: int):
#     if user_id != 1:
#         raise HTTPException(status_code=404, detail="User not found")
#     return {"id": 1, "name": "John Doe"}

