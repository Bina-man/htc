from typing import Optional

from fastapi import FastAPI
from routers import email_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(email_router.router)

@app.get("/check")
async def check():
    return {"message": "The email service is running!"}
