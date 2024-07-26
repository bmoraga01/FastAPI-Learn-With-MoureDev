from fastapi import APIRouter

router = APIRouter(prefix='/products', responses={ 404: {'msg': 'Producto No Encontrado'} }, tags=['Products'])

products = ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4', 'Producto 5']

@router.get('/')
async def get_products():
    return products

@router.get('/{id}')
async def get_product_by_id(id: int):
    return products[id]