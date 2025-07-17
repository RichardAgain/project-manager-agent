
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from src.deepseek import call_deepseek_api


app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_message = data.get("prompt", "")
    # Call your chatbot logic here
    response = call_deepseek_api(user_message)
    print(response)
    return JSONResponse(content={"response": response})

app.mount("/", StaticFiles(directory="./dist", html=True), name="static")
