from fastapi import FastAPI
from routers import email_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Add CORS middleware to allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, you can specify a list of allowed origins instead of '*'
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(email_router.router)

@app.get("/check")
async def check():
    return {"message": "The email service is running!"}
