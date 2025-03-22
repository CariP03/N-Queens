class QueenSolver:
    @staticmethod
    def __validate_pos(candidate: [int], row: int) -> bool:
        val = True

        for i in range(row):
            # Check for column or diagonal threat
            if candidate[row] == candidate[i] or abs(row - i) == abs(candidate[row] - candidate[i]):
                val = False

        return val

    @staticmethod
    def solve(board_size: int):
        # Inner recursive function
        def inner_solve(candidate: [int], row: int) -> ([int], bool):
            found = False  # initialize found

            # Try to add a queen in each column
            for j in range(board_size):
                candidate[row] = j

                # Check if the move is legal
                if QueenSolver.__validate_pos(candidate, row):
                    if row != board_size - 1:
                        candidate, found = inner_solve(candidate, row + 1)  # Try to add a queen in the next row

                    else:
                        # Return a solution and set the found flag to True
                        return candidate, True

                # Check if a solution has been found
                if found:
                    return candidate, True

            # No solution has been found
            return candidate, False

        # Initialize the loop
        empty_solution = [-1] * board_size
        solution, solved = inner_solve(empty_solution, 0)

        # Return a solution if found
        if solved:
            return solution
        else:
            return None
