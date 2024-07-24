from fastapi import FastAPI
from fastapi.responses import JSONResponse
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
async def get_user_list():
    return users_db

@app.get('/users/{id}', tags=['Users'])
async def get_user_by_id(id: int):
    return search_user_by_id(id)
    

@app.get('/userquery', tags=['Users'])
async def get_user(id: int):
    return search_user_by_id(id)
    
@app.post('/users', tags=['Users'], status_code=201)
async def create_user(user: User):
    if type(search_user_by_id(user.id)) == User:
        return JSONResponse(content={ 'error': 'El usuario ya existe' }, status_code=400)
    else:
        users_db.append(user)
        return JSONResponse(content={ 'msg': f'Usuario {user.name} Creado Correctamente' }, status_code=201)
    
# @app.put('/users/{id}', tags=['Users'], status_code=200)
@app.put('/users', tags=['Users'], status_code=200)
# async def update_user(id: int, user: User):
async def update_user(user: User):
    
    found = False
    
    for index, saved_user in enumerate(users_db):
        if saved_user.id == user.id:
            users_db[index] = user
            found = True
    
    if not found:
        return JSONResponse(content={ 'error': 'No se ha encontrado el usuario' }, status_code=404)
    return JSONResponse(content={ 'msg': 'El usuario ha sido actualizado' }, status_code=200)

@app.delete('/users/{id}', tags=['Users'], status_code=200)
async def delete_user(id: int):
    
    found = False
    for index, saved_user in enumerate(users_db):
        if saved_user.id == id:
            del users_db[index]
            found = True
            
    if not found:
        return JSONResponse(content={ 'error': 'No se ha encontrado el usuario' }, status_code=404)
    return JSONResponse(content={ 'msg': 'El usuario ha sido Eliminado' }, status_code=200)
    
def search_user_by_id(id: int) -> dict :
    users = filter( lambda user: user.id == id, users_db )
    
    try:
        return list(users)[0]
    except:
        return { 'error': 'No se ha encontrado el usuario' }
    