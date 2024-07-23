from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return '¡Hola FastAPI!'
    

@app.get('/url')
async def url_curso():
    return {'url_curso': 'https://mouredev.com/python'}