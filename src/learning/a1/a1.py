# DO NOT modify or add any import statements
from support import *


# Name: Shiqi Su
# Student Number: 48771058
# Favorite Tree: B+Tree
# -----------------------------------------------------------------------------

# Define your classes and functions here

# Task 1
def num_hours() -> float:
    """
    Returns:
        float: The number of hours is a floating-point value
    """
    return 11.0


# Task 2
def create_empty_board(board_size: int) -> list[list[str]]:
    """
    Create an empty square board, and empty positions are marked with
    the special symbol: EMPTY from support.py.

    Args:
        board_size (int): Size of the board.

    Returns:
        list[list[str]]: Return a 2-dimensional list representing the empty board,
        each cell is initialized with the empty symbol.

    Preconditions:
        board_size >= 0
    """
    # <editor-fold desc="Wrong code -> Deep Copy & Shallow Copy">
    # empty_board = []
    # inner_board = []
    # if board_size < 0:
    #     return empty_board
    # for _ in range(0, board_size):
    #     inner_board.append(EMPTY)
    # for _ in range(0, board_size):
    #     empty_board.append(inner_board)
    # </editor-fold>

    # The empty is a list of lists.
    empty_board = []
    if board_size < 0:
        return empty_board

    # For each row of the board, create a list of EMPTY cells and add it
    # to empty_board.
    for _ in range(0, board_size):
        row: list[str] = []
        for _ in range(0, board_size):
            row.append(EMPTY)
        empty_board.append(row)

    return empty_board


# Task 3
def display_board(board: list[list[str]]) -> None:
    """
    Display the current state of the board.

    The list of lists needs to show the row number and column number
    for every element.
    - 1. Display each row and column’s sequence number through strings.
    Args:
        board (list[list[str]]): A 2-dimensional list representing the board

    Returns:
        None

    Preconditions:
        1. The board must contain at least one row and one column
        2. Each row of the board will contain the same number of columns.
    """
    col = len(board[0])
    row = len(board)
    #
    print(end="")

    # Print the column numbers and the top-left corner is left blank to align row
    # and column labels.
    for c in range(1, col + 1):
        print('  ' + '  '.join(str(c)), end='')
        if c == col:
            print(end='\n')

    # Print the row numbers
    for r in range(row):
        print(r + 1, end=" ")
        for c in range(col):
            if c > 0:
                print("  ", end="")
            print(board[r][c], end="")
        print(end='\n')


# Task 4
def add_piece(board: list[list[str]], piece: str,
              pos: tuple[int, int]) -> bool:
    """
    Adds the specified piece to the board at the given location
    if valid to do so.

    This function will maintain the latest state of the board, including the
    piece that have already been placed and the empty spots. And the top left
    corner is given by (1,1).

    Args:
        board (list[list[str]]): The current board.
        piece (str): The color represents White or black.
        pos (tuple[int, int]): A target position.

    Returns:
        bool: Return true when a piece successfully added to the board,
        otherwise return false.

    Preconditions:
        The given position must be empty, otherwise the given piece throws an
        exception: 'INVALID_PLACEMENT_MESSAGE' from support.py.
    """
    # Check if this position is empty
    row_index, cols_index = pos
    r = row_index - 1
    c = cols_index - 1
    if board[r][c] == EMPTY:
        board[r][c] = piece
        return True
    else:
        print(INVALID_PLACEMENT_MESSAGE)
        return False


# Task 5
def move_piece(board: list[list[str]], piece: str,
               current_pos: tuple[int, int], target_pos: tuple[int, int]
               ) -> bool:
    """
    Move the specified piece from current_pos to target_pos within board.

    This function checks
    1. If the current position contains the given piece
    2. The target position is empty
    3. The target position is adjacent to the current position.
    If all conditions are satisfied, the piece is moved to the target position,
    and the function returns True. Otherwise, return False.

    Args:
        board (list[list[str]]): The game board represented as a 2D list of
        strings.
        piece (str): The piece to be moved.
        current_pos (tuple[int, int]): The current position of the piece, given
        as a 1-indexed tuple.
        target_pos (tuple[int, int]): The target position to move the piece to.

    Returns:
        bool: If successfully move it, return True. Otherwise, return False.

    Preconditions:
        1. current_pos and target_pos correspond to a position that exists
        within the board.

    """

    # Find the current index of row and column.
    cu_r_index, cu_c_index = current_pos
    cu_r = cu_r_index - 1
    cu_c = cu_c_index - 1

    # Find the target index of row and column.
    ta_r_index, ta_c_index = target_pos
    ta_r = ta_r_index - 1
    ta_c = ta_c_index - 1

    # Check the current position has the same piece
    if board[cu_r][cu_c] != piece:
        print(INVALID_MOVEMENT_MESSAGE)
        return False

    # Check the target position is empty.
    if board[ta_r][ta_c] != EMPTY:
        print(INVALID_MOVEMENT_MESSAGE)
        return False

    # Check target_pos is same with current_pos.
    if cu_c == ta_c and cu_r == ta_r:
        print(INVALID_MOVEMENT_MESSAGE)
        return False

    # Check the target position is adjacent to the current position
    is_adjacent = (
            (cu_r - 1 <= ta_r <= cu_r + 1) and
            (cu_c - 1 <= ta_c <= cu_c + 1))
    if not is_adjacent:
        print(INVALID_MOVEMENT_MESSAGE)
        return False

    # Move piece
    board[cu_r][cu_c] = EMPTY
    board[ta_r][ta_c] = piece
    return True


# Task 6 - Auxiliary Function
def is_command(command: str, command_length: int) -> bool:
    """
    Check if the command is valid
    Args:
        command (str): The command string
        command_length (int): The length of the command.

    Returns:
        bool: True if the part of command is valid. False otherwise.

    """
    for i in range(1, command_length):
        if command[i] not in ('1', '2', '3', '4', '5'):
            return False
    return True


# Task 6
def check_input(command: str) -> bool:
    """
    Validate whether a given command string is in the correct format.

    This function checks if the input command matches one of the valid formats
    (case-insensitive).
        - H / h: Display help message
        - Q / q: Quit the game
        - p[X][Y] / P[X][Y]: Place a piece at row X and column Y (between1-5)
        - m[X][Y][U][V] / M[X][Y][U][V]: Move a piece from (X, Y) to (U, V),
        (between 1-5)

    Args:
        command (str): The command string to be validated. Case-insensitive.

    Returns:
        bool: True if the command is valid. False otherwise.

    """
    # Define constant
    AUXILIARY_LEN = 1
    P_LENGTH = 3
    M_LENGTH = 5
    # The current command length
    command_length = len(command)

    # Check the command length
    if command_length not in (AUXILIARY_LEN, P_LENGTH, M_LENGTH):
        return False

    # Check the command length
    if command_length == 1:
        return command in ('H', 'h', 'Q', 'q')

    # Check other letters of the str
    if command[0] in ('p', 'P') and command_length == P_LENGTH:
        return is_command(command, command_length)

    if command[0] in ('m', 'M') and command_length == M_LENGTH:
        return is_command(command, command_length)
    return False


# Task 7
def get_command() -> str:
    """
    Check if the command is not valid, return a prompt in screen. Then make
    user input again, until the command is valid.

    The function checks if the command is not in the list of move (Q, H is not
    the move command)

    Returns:
        str: A command must be lowercase.

    """
    while True:
        # Input the command
        command = input('Please enter your command (h to see valid command): ')
        # Make sure the command is case-insensitive
        command = command.strip().lower()

        # Check if this command is valid
        is_com = check_input(command)
        # If it is invalid, print a prompt message.
        if not is_com:
            print(INVALID_FORMAT_MESSAGE)
            continue

        # If the command is h or q, return the letter.
        if command in (HELP_COMMAND, QUIT_COMMAND):
            return command
        # others return the result.
        return command


# Task 8 (AI provide a thinking path)
def has_unbroken_line(board: list[list[str]], piece: str) -> bool:
    """
    Check whether the given board ontains an unbroken line of the specified
    piece.

    This function returns if the given board contains an unbroken line
    of the specified piece at least 4 long. The line must be
    horizontal, vertical, or diagonal. Otherwise, return False.

    Args:
        board (list[list[str]]): A given board to be checked.
        piece (str): The specified player's piece

    Returns:
        bool: True, the unbroken line has length 4. Otherwise, false.

    """

    # Limit the length of unbroken line
    UNBROKEN_LINE_LEN = 4
    ERROR_LEN = 0

    #  Verity the row and column of the board
    row = len(board)
    if row == ERROR_LEN:
        return False

    col = len(board[0])
    if col == ERROR_LEN:
        return False

    # Check if the line is horizontal
    for r in range(row):
        step = 0
        for c in range(col):
            if board[r][c] == piece:
                step += 1
                if step >= UNBROKEN_LINE_LEN:
                    return True
            else:
                step = 0

    # Check if the line is vertical
    for c in range(col):
        step = 0
        for r in range(row):
            if board[r][c] == piece:
                step += 1
                if step == UNBROKEN_LINE_LEN:
                    return True
            else:
                step = 0

    # Check if the line is left diagonal, iterate with column.
    for c0 in range(col):
        r, c, step = 0, c0, 0
        while r < row and c < col:
            if board[r][c] == piece:
                step += 1
                if step >= UNBROKEN_LINE_LEN:
                    return True
            else:
                step = 0
            r += 1
            c += 1

    # Iterate with row.
    for r0 in range(1, row):
        r, c, step = r0, 0, 0
        while r < row and c < col:
            if board[r][c] == piece:
                step += 1
                if step >= UNBROKEN_LINE_LEN:
                    return True
            else:
                step = 0
            r += 1
            c += 1

    # Check if the line is right diagonal, iterate with column.
    for c0 in range(col):
        r, c, step = row - 1, c0, 0
        while r >= 0 and c < col:
            if board[r][c] == piece:
                step += 1
                if step >= UNBROKEN_LINE_LEN:
                    return True
            else:
                step = 0
            r -= 1
            c += 1

    # Iterate with row.
    for r0 in range(row - 2, -1, -1):
        r, c, step = r0, 0, 0
        while r >= 0 and c < col:
            if board[r][c] == piece:
                step += 1
                if step >= UNBROKEN_LINE_LEN:
                    return True
            else:
                step = 0
            r -= 1
            c += 1
    return False


# Task 9 - (AI provide a thinking path)
def has_square(board: list[list[str]], piece: str) -> bool:
    """
    Check whether the specified piece composes a square (2*2).

    Args:
        board (list[list[str]]): A given board to be checked.
        piece (str): The different piece symbol

    Returns:
        bool: If the same piece composes a square, return True.
        Otherwise, return False

    """
    # Check if the board size is 0
    if not board or not board[0]:
        return False

    row = len(board)
    col = len(board[0])

    # The board must over 2 * 2
    if row < 2 or col < 2:
        return False

    # Check every left-top piece, whether it can compose a square
    for r in range(row - 1):
        for c in range(col - 1):
            if (board[r][c] == piece and
                    board[r][c + 1] == piece and
                    board[r + 1][c] == piece and
                    board[r + 1][c + 1] == piece):
                return True

    return False


# Task 10
def check_win(board: list[list[str]]) -> str:
    """
    Determine which player has won the game.

    This function inspects the given board state to check whether a player
    has achieved a winning condition. A player wins if they form wither:
    1. An unbroken line at least 4 pieces or a square
    2.
    Args:
        board (list[list[str]]): The current status of the board

    Returns:
        str: The piece of the winning player. Otherwise, return an empty
    board.

    """
    p1 = PLAYER_1_PIECE
    p2 = PLAYER_2_PIECE
    p1_win = has_unbroken_line(board, p1) or has_square(board, p1)
    p2_win = has_unbroken_line(board, p2) or has_square(board, p2)

    if p1_win:
        return p1
    elif p2_win:
        return p2
    else:
        return EMPTY


# Task 11 - Auxiliary Function - Convert the place index to int
def convert_place(cmd: str) -> tuple[int, int]:
    cmd = cmd.lower()
    return int(cmd[1]), int(cmd[2])


# Task 11 - Auxiliary Function - Covert the move index to int
def convert_move(cmd: str) -> tuple[tuple[int, int], tuple[int, int]]:
    cmd = cmd.lower()
    return (int(cmd[1]), int(cmd[2])), (int(cmd[3]), int(cmd[4]))


# Task 11 - AI provide a thinking path and fix logic bug
def play_game() -> None:
    """
    The game from beginning to end.
    1. Create a 5*5 empty board
    2. Display a welcoming for both players.
    3. Display the board, then if there also are remained pieces, print the remain number
    4. Input command then add/move a piece.
    5. Check the game state. If won, return the piece of winner. Others return to
    the 2nd step.
    Returns:
        str: The piece of winner.

    """
    # Initial information of board and players.
    current_board = create_empty_board(BOARD_SIZE)
    p_left = {1: NUM_PLAYER_PIECES, 2: NUM_PLAYER_PIECES}
    piece_color = {1: PLAYER_1_PIECE, 2: PLAYER_2_PIECE}
    player_name = {1: PLAYER_1_DISPLAY, 2: PLAYER_2_DISPLAY}

    print(WELCOME_MESSAGE)

    # Beginning of the first player
    current = 1

    while True:
        # 1. Display the current board
        display_board(current_board)
        while True:
            # 2. Display prompt which player put their piece and remain number.
            print(player_name[current] + turn_message(p_left[current]))
            # 3. Input a command and check if it is valid.
            cmd = get_command()

            # Demonstrate the help message.
            if cmd == HELP_COMMAND:
                print(HELP_MESSAGE)
                continue
            # Q will exit the game.
            if cmd == QUIT_COMMAND:
                return

            # 4. Check if the cmd needs to put (pXY)
            if cmd[0] == PLACE_COMMAND:
                # Whether it has remained pieces
                if p_left[current] == 0:
                    print(ALREADY_PLACED_MESSAGE)
                    continue
                # Add a piece to board
                pos = convert_place(cmd)
                ok = add_piece(current_board, piece_color[current], pos)
                if not ok:
                    continue
                # The number of remained piece minus 1
                p_left[current] -= 1
                break

            # Check if the cmd is movement (mXYUV)
            elif cmd[0] == MOVE_COMMAND:
                # Whether it has remained pieces
                if p_left[current] > 0:
                    print(MUST_PLACE_MESSAGE)
                    continue
                # Move the piece to target position
                cur_pos, tar_pos = convert_move(cmd)
                ok = move_piece(current_board, piece_color[current], cur_pos, tar_pos)
                if not ok:
                    continue
                break
            else:
                # Check if there is another invalid situation
                continue

        # 5. Check the game result. If won, finish the game and output
        # the piece of winner. Otherwise, continue games.
        winner_piece = check_win(current_board)
        if winner_piece != EMPTY:
            display_board(current_board)
            print(player_name[current])
            return
        if current == 1:
            current = 2
        else:
            current = 1


def main() -> None:
    """
    Check if the whole game can normally run. The Console will provide a
    board then two players can begin games.

    Returns:
        None

    """
    while True:
        # Continue the whole game
        play_game()

        # Ask player if he/she wants to start a new game.
        ans = input(AGAIN_PROMPT).strip()

        # Input is y, continue another game. Otherwise, finish the game.
        if ans.lower() != 'y':
            break


if __name__ == "__main__":
    main()
