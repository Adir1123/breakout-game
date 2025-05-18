from tkinter import *

class GameWindow:
    def __init__(self,height, width, title="Breakout Game"):
        self.window = Tk()
        self.window.title(title)
        self.window.resizable(False,False)
        self.canvas = Canvas(self.window, width=width, height=height, bg="black")
        self.canvas.pack()


    def run(self):
        self.window.mainloop()

