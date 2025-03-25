from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/price")
async def get_price():
    
    filename = "./json/price.json" 
    with open(filename, "r") as f:
        data = json.load(f) 
    return data
    