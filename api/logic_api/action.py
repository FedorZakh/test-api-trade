import asyncio
from params import *

CURRENT_PRICE = START_PRICE

async def price_generator(end_price=END_PRICE,start_price=START_PRICE,step=STEP):
    global current_price, direction
    while True:
        if current_price >= end_price:
            direction = -1
        elif current_price <= start_price:
            direction = 1
        current_price += direction * step
        await asyncio.sleep(1)