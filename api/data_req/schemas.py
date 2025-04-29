from pydantic import BaseModel


class OrderSave(BaseModel):
    name: str
    order_price: float
