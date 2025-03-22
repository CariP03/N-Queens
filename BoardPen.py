import turtle as t

class BoardPen:
    # Private attributes
    __SQUARE_SIZE = 30  # measured in pixels

    t.speed(0)  # set the speed of the turtle to the maximum value

    @staticmethod
    def __draw_square():
        # Draw each side
        for i in range(4):
            t.forward(BoardPen.__SQUARE_SIZE)  # draw one side
            t.left(90)  # turn left 90 degrees to prepare for the next side

        t.forward(BoardPen.__SQUARE_SIZE)  # move to the next square

    @staticmethod
    def __to_next_line(size: int):
        # Move to the start of the new row
        t.left(90)
        t.forward(BoardPen.__SQUARE_SIZE)

        t.left(90)
        t.forward(size * BoardPen.__SQUARE_SIZE)

        t.right(180)

    @staticmethod
    def draw_board(size: int):
        # Avoid animation
        t.tracer(1, 0)

        # Set initial position
        initial_pos = -size * BoardPen.__SQUARE_SIZE / 2

        t.penup()
        t.setpos(initial_pos, initial_pos)
        t.pendown()

        for i in range(size):
            for j in range(size):

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

            BoardPen.__to_next_line(size)

        # End drawing
        t.hideturtle()
        t.mainloop()
