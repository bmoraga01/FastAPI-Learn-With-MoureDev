from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter(prefix='/users', tags=['Users'])

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

@router.get('/')
async def get_user_list():
    return users_db

@router.get('/{id}')
async def get_user_by_id(id: int):
    return search_user_by_id(id)
    

@router.get('/userquery')
async def get_user(id: int):
    return search_user_by_id(id)
    
@router.post('/', status_code=201, response_model=User)
async def create_user(user: User) -> JSONResponse:
    if type(search_user_by_id(user.id)) == User:
        raise HTTPException(status_code=204, detail='El usuario ya existe')
    else:
        users_db.append(user)
        # return JSONResponse(content={ 'msg': f'Usuario {user.name} Creado Correctamente' }, status_code=201)
        return user
    
# @app.put('/users/{id}', status_code=200)
@router.put('/', status_code=200)
# async def update_user(id: int, user: User):
async def update_user(user: User) -> JSONResponse:
    
    found = False
    
    for index, saved_user in enumerate(users_db):
        if saved_user.id == user.id:
            users_db[index] = user
            found = True
    
    if not found:
        raise HTTPException(status_code=404, detail='No se ha encontrado el usuario')
    return JSONResponse(content={ 'msg': 'El usuario ha sido actualizado' }, status_code=200)

@router.delete('/{id}', status_code=200)
async def delete_user(id: int) -> JSONResponse:
    
    found = False
    for index, saved_user in enumerate(users_db):
        if saved_user.id == id:
            del users_db[index]
            found = True
            
    if not found:
        raise HTTPException(status_code=404, detail='No se ha encontrado el usuario')
    return JSONResponse(content={ 'msg': 'El usuario ha sido Eliminado' }, status_code=200)
    
def search_user_by_id(id: int) -> dict :
    users = filter( lambda user: user.id == id, users_db )
    
    try:
        return list(users)[0]
    except:
        return { 'error': 'No se ha encontrado el usuario' }
    