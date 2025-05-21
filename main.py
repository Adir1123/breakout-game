
from game_window import GameWindow
from paddle import Paddle
from ball import Ball
from bricks import Bricks

game = GameWindow(600, 800)

paddle = Paddle(game.canvas)
ball = Ball(game.canvas,paddle)

bricks = []
rows = 5
cols = 10
padding = 5
brick_width = (int(game.canvas["width"]) - (cols + 1) * padding) / cols
brick_height = 20
colors = ["red", "orange", "yellow", "green", "purple"]

for row in range(rows):
    y = padding + row * (brick_height + padding)
    for col in range(cols):
        x = padding + col * (brick_width + padding)
        bricks.append(
            Bricks(game.canvas, x, y, width=brick_width, height=brick_height, color=colors[row % len(colors)])
        )

def animate():
    ball.draw()
    for brick in bricks[:]:  # iterate over a copy
        if brick.collide(ball):
            bricks.remove(brick)
            break

    if not ball.hit_bottom:
        game.canvas.after(20, animate)

animate()
game.run()





