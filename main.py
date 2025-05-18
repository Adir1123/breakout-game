from tkinter import *
from game_window import GameWindow
from paddle import Paddle

game = GameWindow(600, 800)

paddle = Paddle(game.canvas)

game.run()





