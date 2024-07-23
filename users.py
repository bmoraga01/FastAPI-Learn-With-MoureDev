from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int
    
users_db = [
    User(id=1, name = 'Brais', surname = 'Moure', url = 'https://moure.dev', age = 35),
    User(id=2, name = 'Moure', surname = 'Dev', url = 'https://mouredev.com', age = 53 ),
    User(id=3, name = 'Haakon', surname = 'Dahlberg', url = 'https://haakon.com', age = 20 )
]

@app.get('/users', tags=['Users'])
def get_user_list():
    return users_db

@app.get('/users/{id}', tags=['Users'])
def get_user(id: int):
    return [ x for x in users_db if x.id == id ]