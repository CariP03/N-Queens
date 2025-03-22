import turtle

from BoardPen import BoardPen
from QueenSolver import QueenSolver

if __name__ == '__main__':
    size = 50

    # Solve the problem
    board = QueenSolver.solve(size)

    # Print the solution
    print(board)

    # Draw the solution
    if board is not None:
        pen = BoardPen(size)
        pen.draw_board()
        pen.populate_board(board)

        turtle.mainloop()
