

class Bricks:
    def __init__(self,canvas, x, y, width=75, height=20, color="blue"):
        self.canvas = canvas
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.id = canvas.create_rectangle(
            x, y,
            x + width, y + height,
            fill=color, outline="white"
        )

    def delete(self):
        self.canvas.delete(self.id)


    def collide(self,ball):
        brick_pos = self.canvas.coords(self.id)
        pos = self.canvas.coords(ball.id)

        horiz = (pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2])
        vert = (pos[1] <= brick_pos[3] and pos[3] >= brick_pos[1])

        if horiz and vert:
            self.delete()
            ball.y_speed = abs(ball.y_speed)
            return True

        return False

