from fastapi import APIRouter
# import json
from logic_api.action import get_price
from logic_api.params import *

router = APIRouter()

@router.get("/price")
def test():
    return get_price()
    
    # filename = "./json/price.json" 
    # with open(filename, "r") as f:
    #     data = json.load(f) 
    # return data
    