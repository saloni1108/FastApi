# import sys

# sys.path.append('C:\\Users\\ragar\\Desktop\\BridgeLabz_tasks\\FastApi\\FastApi\\fastapi-venv\\Lib\\site-packages')

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return "Hello World!"

@app.post('/')
def post_root():
    return "hellow from the post route"

users = {
    1: {"name": "John Doe", "email": "john.doe@example.com"},
    2: {"name": "Jane Smith", "email": "jane.smith@example.com"},
}

@app.get('/users')
def list_items():
    return "list of route users"

@app.get('/users/user_id')
def get_item(user_id):
    return {"user_id": user_id}
