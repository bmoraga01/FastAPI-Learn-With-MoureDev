from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import products, users

app = FastAPI()

# Routers
app.include_router(users.router)
app.include_router(products.router)

@app.get('/', tags=['Main'])
async def index():
    return RedirectResponse(url='/docs')

# @app.get('/', tags=['Main'])
# async def root():
#     return '¡Hola FastAPI!'
    

@app.get('/url', tags=['Main'])
async def url_curso():
    return {'url_curso': 'https://mouredev.com/python'}