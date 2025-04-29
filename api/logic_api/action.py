import asyncio
from logic_api.params import *
import logging


logging.basicConfig(level=logging.INFO)

CURRENT_PRICE = START_PRICE


def get_price():
    return CURRENT_PRICE


async def price_generator(
    end_price=END_PRICE, start_price=START_PRICE, step=STEP, direction=DIRECTION
):
    global CURRENT_PRICE

    while True:
        if CURRENT_PRICE >= end_price:
            direction = -1
        elif CURRENT_PRICE <= start_price:
            direction = 1

        CURRENT_PRICE += direction * step

        logging.info(f"Updated price: {CURRENT_PRICE}")
        await asyncio.sleep(1)
