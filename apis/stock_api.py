from fastapi import APIRouter

from utils.stock_alpha import result_stock

router = APIRouter()


@router.get('/')
async def all_list_stock():
    return True


@router.post('/add_stock')
async def add_stock(stock: str, action: str):
    return result_stock(stock_name=stock, information=action)


@router.delete('/remove_stock')
async def remove_stock(payload: str):
    return True


@router.put('/update_stock')
async def update_stock(payload):
    return True
