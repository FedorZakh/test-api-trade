from fastapi import APIRouter
from data_req.queries import DatabaseManager
from data_req.schemas import OrderSave
from logic_api.action import get_price
from logic_api.params import *

router = APIRouter()
db = DatabaseManager("database.db")


@router.get("/price")
def test():
    return get_price()


@router.post("/order_buy")
def add_order_buy(order: OrderSave):
    db.create_table_levels()
    db.add_order_buy(order.name, order.order_price, order.quantity)
    return {"status": "ok", "message": "Order buy added"}


@router.post("/order_sell")
def add_order_sell(order: OrderSave):
    db.create_table_levels()
    db.add_order_sell(order.name, order.order_price, order.quantity)
    return {"status": "ok", "message": "Order buy added"}
