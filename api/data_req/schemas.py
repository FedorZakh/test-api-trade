from pydantic import BaseModel


class OrderRequest(BaseModel):
    name: str
    order_price: float
