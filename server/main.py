from typing import Optional

from fastapi import FastAPI

app = FastAPI()


origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api/todo")
async def read_todo():
    return 1

@app.post("/api/todo/")
async def post_todo(todo):
    return 1

@app.put("/api/todo{id}")
async def put_todo(id, data):
    return 1

@app.get("/api/todo{id}")
async def get_todo

@app.delete("/api/todo{id}")
async def delete_todo