import random
import math
from tkinter import *
from tkinter import ttk

root = Tk() #the main window
gameBoard = Frame(root) #the widget containing the tiles
gameBoard.grid(row=0, column=1)

gameTitleLabel = Label(root, text='Minesweeper')
gameTitleLabel.grid(row=0, column=0)

#gameTitleLabel.pack() # do not need to pack if you are using grid

class Tile(Label):
    hasbomb = False
    flagged = False
    neighborbombcount = 0
    def __init__(self, master, text, bomb):
        Label.__init__(self, master, text=text)
        self.hasbomb = bomb
        self.neighborbombcount = 0
    def setbomb(self, bombbool):
        self.hasbomb = bombbool
    def incrbombcount(self):
        self.neighborbombcount += 1
    def revealsim(self):
        if self.hasbomb:
            self.config(text="[_B_]")
        else:
            self.config(text="[   ]")

def Reveal(event):
    if(event.widget.flagged == False):
        if(event.widget.hasbomb):
            event.widget.config(text='[_B_]')
        else:
            #here if revealing a tile that is NOT a bomb
            event.widget.config(text=event.widget.neighborbombcount)

def Flag(event):
    if event.widget.flagged:
        #here if the clicked tile is flagged already, but user wants to unflag it
        event.widget.config(text='[___]')
        event.widget.flagged = False
    else:
        #here if the clicked tile is not flagged, but user wants it flagged
        event.widget.flagged = True
        event.widget.config(text='[_F_]')

tilelist = list() #define a new list to hold all the game tiles

def calcNeighbors(gridSize):
    for i in range(len(tilelist)):
        #look at every tile, then look at all eight neighbors and increment curr tile bomb count
        r = math.floor(i / gridSize)
        c = i % gridSize
        isleftedge = (c == 0)
        isrightedge = (c == gridSize - 1)

        if i > 0 and isleftedge == False and tilelist[i -1].hasbomb: tilelist[i].incrbombcount()
        if i > 9 and isrightedge == False and tilelist[i +1 -gridSize].hasbomb: tilelist[i].incrbombcount()
        if i > 10 and tilelist[i -gridSize].hasbomb: tilelist[i].incrbombcount()
        if i > 11 and isleftedge == False and tilelist[i -1 -gridSize].hasbomb: tilelist[i].incrbombcount()
        if i < 98 and isrightedge == False and tilelist[i +1].hasbomb: tilelist[i].incrbombcount()
        if i < 90 and isleftedge == False and tilelist[i -1 +gridSize].hasbomb: tilelist[i].incrbombcount()
        if i < 88 and isrightedge == False and tilelist[i +1 +gridSize].hasbomb: tilelist[i].incrbombcount()
        if i < 89 and tilelist[i +gridSize].hasbomb: tilelist[i].incrbombcount()

def newGame(gridSize):
    tilecount = gridSize * gridSize
    totalbombs = 16
    newtilelist = list()
    newtilelist.clear()
    for i in range(totalbombs):
        newtilelist.append(True)
    while len(newtilelist) < tilecount:
        newtilelist.append(False)

    random.shuffle(newtilelist) #randomize the bombs
    tilelist.clear()

    for x in range(tilecount):
        newTile = Tile(gameBoard, '[___]', newtilelist[x] )
        newTile.config(font=('Trebuchet MS',12))
        newTile.bind('<Button-1>', Reveal)
        newTile.bind('<Button-3>', Flag)
        r = math.floor(x / gridSize)
        c = x % gridSize
        newTile.revealsim()
        newTile.grid(row=r, column=c+1)
        tilelist.append(newTile) #add the new tile to the game board list

    calcNeighbors(gridSize)

newGame(10)
root.geometry('650x400')
root.mainloop()