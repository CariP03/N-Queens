import turtle

from BoardPen import *

if __name__ == '__main__':
    board = BoardPen(8)
    board.draw_board()

    board.place_queen(7, 7)

    turtle.mainloop()
