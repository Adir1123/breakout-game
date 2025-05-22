

class Paddle:
    def __init__(self, canvas, width=100, height=20, color="white", y_offset=40):
        self.canvas = canvas # the paddle
        self.width = width # paddle width
        self.height = height # paddle height
        self.color = color
        self.y_offset = y_offset

        self.canvas_width = int(self.canvas["width"]) # width of the screen
        self.canvas_height = int(self.canvas["height"]) # height of the screen

        start_x = (self.canvas_width - self.width) / 2
        start_y = self.canvas_height - self.y_offset


        self.id = self.canvas.create_rectangle( # the actual paddle
            start_x, start_y,
            start_x + self.width, start_y + self.height,
            fill=self.color
        )

        self.move_speed = 20
        self.canvas.bind_all("<Left>",self.move_left)
        self.canvas.bind_all("<Right>", self.move_right)

    def move_left(self, event=None):
        cords = self.canvas.coords(self.id) # gets the x1 y1 x2 y2 of the rectangle
        if cords[0] > 20: # if the left corner of the rectangle "cords[0]"
                          # doesn't touch the edge of the left screen "0", you can move.
            self.canvas.move(self.id, -self.move_speed, 0) # move the rectangle -20 (left) in x, y=0 doesn't move

    def move_right(self, event=None):
        cords = self.canvas.coords(self.id)
        if cords[2] < self.canvas_width - 20: # if the right corner of the paddle x2 "cords[2]"
                                              # doesn't touch the edge of the right screen "self.canvas_width",
                                              # you can move to the right
            self.canvas.move(self.id, self.move_speed, 0)