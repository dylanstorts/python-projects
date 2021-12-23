import tkinter
from tile import Tile
import random

GRID_WIDTH = 16
GRID_HEIGHT = 8
NUM_BOMBS = 20

def generate_tiles(tiles, width, height):
    for x in range(width):
        for y in range(height):
            new_btn = Tile("#")
            new_btn.bind("<Button-3>", flagging)
            tiles.append(new_btn)

def plant_bombs(tiles, bombs_to_make):
    for i in range(bombs_to_make):
        tiles[i].bomb = True
        tiles[i].config(text=tiles[i].bomb_text)
    random.shuffle(tiles)

def generate_grid(tiles, width, height):
    index = 0
    for x in range(width):
        for y in range(height):
            tiles[index].grid(row=y, column=x, padx=2, pady=2)
            tiles[index].xcor = x
            tiles[index].ycor = y
            index += 1



def flagging(event):
    event.config(text="red")

window = tkinter.Tk()
window.title("PySweeper")


tiles = []
generate_tiles(tiles, GRID_WIDTH, GRID_HEIGHT)
plant_bombs(tiles, NUM_BOMBS)
generate_grid(tiles, GRID_WIDTH, GRID_HEIGHT)


window.mainloop()
