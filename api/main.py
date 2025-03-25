from fastapi import FastAPI
from contextlib import asynccontextmanager
from routing import price
from logic_api.action import price_generator
import asyncio




@asynccontextmanager
async def lifespan(app: FastAPI):
    
    task = asyncio.create_task(price_generator())  
    yield
    task.cancel()  

app = FastAPI(lifespan=lifespan)

app.include_router(price.router)
