from fastapi import APIRouter
from logic_api.action import CURRENT_PRICE
router = APIRouter()



@router.get("/price")
def get_price():
    return [CURRENT_PRICE]