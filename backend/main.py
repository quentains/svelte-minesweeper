from random import randint, choice
from math import ceil

from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

def count_bombs(x, y, bombs) :
    n = 0
    for i in range(x-1, x+2) :
        for j in range(y-1, y+2) :
            if (i,j) in bombs :
                n += 1          
    return n
                

def create_game(width, height) :
    game = [[0 for _ in range(width)] for _ in range(height)]
    
    bombs = set()
    nb_bombs = ceil((width * height) / 6.0)
    # Generate random bombs
    while len(bombs) < nb_bombs :
        x = randint(0, width - 1)
        y = randint(0, height - 1)
        bombs.add((x,y))

    # Add the bomb
    for bomb in bombs :
        game[bomb[1]][bomb[0]] = -1
    
    empty = []
    # Compute the other cases
    for x in range(width) :
        for y in range(height) :
            if (x,y) not in bombs :
                game[y][x] = count_bombs(x, y, bombs)
                if game[y][x] == 0 :
                    empty.append((x, y))

    return game, choice(empty)

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
    game, starting_point = create_game(width, height)
    return {'board': game, 'starting_point': {'x': starting_point[0], 'y': starting_point[1]}}
