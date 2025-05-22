

class Ball:
    def __init__(self, canvas, paddle, radius = 10, color = "red", x_speed = 5 ,y_speed = -5): # gets "paddle" to know
                                                                                               # where to locate the ball
                                                                                               # gets "canvas" to know
                                                                                               # the limits of the screen
        self.canvas = canvas
        self.paddle = paddle
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.id = canvas.create_oval(0,0,radius*2,radius*2,fill="lightblue", outline="black") # The ball

        self.canvas_width = int(canvas["width"])
        self.canvas_height = int(canvas["height"])

        paddle_cords = canvas.coords(paddle.id) # gets the cords of the paddle to locate the ball the right way
        start_x = (paddle_cords[0] + paddle_cords[2]) / 2 - radius
        start_y = paddle_cords[1] - radius*2
        canvas.move(self.id, start_x, start_y) # starting the ball near the paddle

        self.hit_bottom = False


    def draw(self):

        self.canvas.move(self.id, self.x_speed, self.y_speed)
        pos = self.canvas.coords(self.id) # the cords x1, y1, x2, y2 of the ball

        #checks collision between ball the walls
        if pos[0] <= 0: # the left screen
            self.x_speed = abs(self.x_speed) # if the ball touches the left screen, bounce to the right +x
        if pos[2] >= self.canvas_width: # if the ball touches the right screen, bounce to the left -x
            self.x_speed = -abs(self.x_speed)
        if pos[1] <= 0:
            self.y_speed = abs(self.y_speed)


        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

        # checks collision between ball the paddle
        paddle_pos = self.canvas.coords(self.paddle.id)
        if (pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] and # x1, y1, x2, y2
                pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]):
            self.y_speed = -abs(self.y_speed)


    def _animate(self):
        if not self.hit_bottom:
            self.draw()
            self.canvas.after(20, self._animate) # calls animate again after 20 sec

    def start(self):
        self.hit_bottom = False
        self._animate()