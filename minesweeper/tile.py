from tkinter import Button
import random

class Tile(Button):

    def __init__(self, txt):
        super().__init__()
        self.config(text=txt)
        self.xcor = 0
        self.ycor = 0
        self.bomb = False
        self.bomb_text = "💣"
        self.flag_text = "🏴"