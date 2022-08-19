from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.v1 import router as v1_router

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

app.include_router(v1_router, prefix="/v1", tags=["v1"])
