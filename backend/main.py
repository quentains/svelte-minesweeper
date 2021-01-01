from random import randint

from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

def create_game(width, height) :
    nb_cases = width * height
    nb_bombs = nb_cases // 10
    
    bombs = set()
    while len(bombs) < nb_bombs :
        bombs.add(randint(0, nb_cases - 1))

    # TODO
    pass

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

@app.get("/new_game/")
async def image(width: int = 16, height: int = 16):
    game = []
    for _ in range(height) :
        game.append([])
        for _ in range(width) :
            game[-1].append(randint(-1,3))
    return game