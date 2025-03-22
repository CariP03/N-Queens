import turtle as t


class BoardPen:
    # Class attributes
    __SQUARE_SIZE = 30  # measured in pixels
    __QUEEN_PATH = "resources/Queen.gif"

    # Class configuration
    t.speed(0)  # set the speed of the turtle to the maximum value
    t.register_shape(__QUEEN_PATH)  # add the shape of the queen

    # Constructor
    def __init__(self, board_size: int):
        self.size = board_size

    @staticmethod
    def __draw_square():
        # Draw each side
        for i in range(4):
            t.forward(BoardPen.__SQUARE_SIZE)  # draw one side
            t.left(90)  # turn left 90 degrees to prepare for the next side

        t.forward(BoardPen.__SQUARE_SIZE)  # move to the next square

    def __to_next_line(self):
        # Move to the start of the new row
        t.left(90)
        t.forward(BoardPen.__SQUARE_SIZE)

        t.left(90)
        t.forward(self.size * BoardPen.__SQUARE_SIZE)

        t.right(180)

    def draw_board(self):
        # Avoid animation
        t.tracer(1, 0)

        # Set initial position
        initial_pos = -self.size * BoardPen.__SQUARE_SIZE / 2

        t.penup()
        t.setpos(initial_pos, initial_pos)
        t.pendown()

        for i in range(self.size):
            for j in range(self.size):

                # Fill square
                t.begin_fill()
                # Determine colour
                if (i + j) % 2 == 0:
                    t.fillcolor("black")

                else:
                    t.fillcolor("white")

                BoardPen.__draw_square()

                t.end_fill()
                t.update()

            BoardPen.__to_next_line(self)

        # End drawing
        t.hideturtle()

    def __calculate_center(self, row: int, col: int) -> (int, int):
        initial_pos = -self.size * BoardPen.__SQUARE_SIZE / 2  # leftmost bottom pixel of the board

        x = initial_pos + col * BoardPen.__SQUARE_SIZE + BoardPen.__SQUARE_SIZE / 2
        y = initial_pos + row * BoardPen.__SQUARE_SIZE + BoardPen.__SQUARE_SIZE / 2

        return x, y

    def place_queen(self, row: int, col: int):
        t.shape(BoardPen.__QUEEN_PATH)  # set the turtle to draw a queen
        center = BoardPen.__calculate_center(self, row, col)

        # move to the center
        t.penup()
        t.setpos(center)
        t.pendown()

        # Draw the queen
        t.stamp()
