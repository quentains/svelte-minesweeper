from random import randint

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

class Game(BaseModel):
    board: List[List[int]] = []

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://localhost:5000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/new_game/", response_model=Game)
async def image(width: int = 16, height: int = 16):
    game = {'board' : []}
    
    for _ in range(height) :
        game['board'].append([])
        for _ in range(width) :
            game['board'][-1].append(randint(-1,3))

    return game