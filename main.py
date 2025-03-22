import time
import turtle

from BoardPen import BoardPen
from QueenSolver import QueenSolver

if __name__ == '__main__':
    size = 8

    # Solve the problem
    board = QueenSolver.one_solve(size)

    # Print the solution
    print(board)

    # Draw the solution
    pen = BoardPen(size)
    if board is not None:
        pen.draw_board()
        pen.populate_board(board)

        time.sleep(5)

    # Find all solutions
    all_boards = QueenSolver.all_solve(size)

    # Print all solutions
    print("Returned " + str(len(all_boards)) + " solutions")
    print(all_boards)

    # Draw all solutions
    for board in all_boards:
        turtle.clear()

        pen.draw_board()
        pen.populate_board(board)
        time.sleep(1)
