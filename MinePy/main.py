from tkinter import *
from tkinter import ttk

class Tile(Label):
    hasbomb = False
    def __init__(self, master, text, bomb):
        Label.__init__(self, master, text=text)
        self.hasbomb = bomb

root = Tk()

gameTitleLabel = Label(root, text='Minesweeper')
gameTitleLabel.grid(row=0, column=0)
#gameTitleLabel.pack() # do not need to pack if you are using grid

def Reveal(event):
    print(event.widget.hasbomb)

def Flag(event):
    print(event.widget.hasbomb)

gameGrid = list() #define a new list to hold all the game tiles
for y in range(10):
    #root.columnconfigure(y, minsize=30)
    for x in range(10):
        #root.rowconfigure(x, minsize=30)
        currentcount = gameGrid.__len__()
        newTile = Tile(root, currentcount, False)
        newTile.config(padx=10)
        newTile.bind('<Button-1>', Reveal)
        newTile.bind('<Button-3>', Flag)
        newTile.grid(row=y, column=x+1)
        gameGrid.append(newTile) #add the new tile to the game board list

root.geometry('650x400')
root.mainloop()