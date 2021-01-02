from random import randint
from math import ceil

from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

def count_bombs(x, y, width, height, game) :
    bombs = 0
    for i in range(x-1, x+2) :
        for j in range(y-1, y+2) :
            if (i, j) != (x, y) :
                if 0 <= i < width and 0 <= j < height :
                    if game[j][i] == -1 :
                        bombs += 1
                        
    return bombs
                

def create_game(width, height) :
    game = [[0 for _ in range(width)] for _ in range(height)]

    bombs = set()
    nb_bombs = ceil((width * height) / 10.0)
    # Generate random bombs
    while len(bombs) < nb_bombs :
        x = randint(0, width - 1)
        y = randint(0, height - 1)
        bombs.add((x,y))

    for bomb in bombs :
        game[bomb[1]][bomb[0]] = -1
        
    for x in range(width) :
        for y in range(height) :
            if (x,y) not in bombs :
                game[y][x] = count_bombs(x, y, width, height, game)

    return game

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
    game = create_game(width, height)
    return game