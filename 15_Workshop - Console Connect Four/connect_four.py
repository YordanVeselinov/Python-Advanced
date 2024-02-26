class InvalidColumn(Exception):
    pass


class FullColumnError(Exception):
    pass


class InvalidAnswerForPlayAgain(Exception):
    pass


def travel_direction(coordinates, current_row, current_col, element, sign, board):
    count = 0
    row_direction, col_direction = coordinates

    for i in range(1, MAXIMUM_CONNECTIONS):
        next_element_row_index = eval(f"{current_row} {sign} {row_direction} * {i}")
        next_element_col_index = eval(f"{current_col} {sign} {col_direction} * {i}")

        try:
            if board[next_element_row_index][next_element_col_index] == element:
                count += 1
            else:
                return count
        except IndexError:
            return count
    return count


def winner_found(current_row, current_col, matrix):
    for direction, coords in DIRECTION_MAPPER.items():
        searched_element = matrix[current_row][current_col]
        travel_direction_count = travel_direction(coords, current_row, current_col, searched_element, "+", matrix)
        travel_opposite_direction_count = travel_direction(coords, current_row, current_col, searched_element, "-",
                                                           matrix)

        if travel_direction_count + travel_opposite_direction_count + 1 >= MAXIMUM_CONNECTIONS:
            return True
    else:
        return False


def check_valid_answer_to_play_again(choice_answer):
    if choice_answer.lower() in ["y", "n"]:
        return True
    raise InvalidAnswerForPlayAgain


def choice_to_play_again():
    while True:
        try:
            choice_to_play = input("Do you want to play again? (Y or N): ")
            if check_valid_answer_to_play_again(choice_to_play):
                if choice_to_play.lower() == "y":
                    return True
                return False
        except InvalidAnswerForPlayAgain:
            print(f"Invalid answer, please select Y or N !")


def validate_column(current_col):
    if 0 <= current_col < COLS:
        return True
    raise InvalidColumn


def print_matrix(matrix):
    [print(f"[ {', '.join(row)} ]") for row in matrix]


def get_available_row(col_index, board_game):
    for row_index in range(ROWS - 1, -1, -1):
        if board_game[row_index][col_index] == '0':
            return row_index
    else:
        raise FullColumnError


def creating_board(rols, cols):
    return [["0" for y in range(COLS)] for x in range(ROWS)]


ROWS, COLS = 6, 7
MAXIMUM_CONNECTIONS = 4

board = creating_board(ROWS, COLS)
turns = 1

print(f"Welcome to connect four console game!")
print(f"The rules are:\n"
      f"1. First player to connect four wins.\n"
      f"2. You can chose a column that has at least one 0\n")
print(f'This is the board!')
print_matrix(board)
print("--- Good luck! ---")

DIRECTION_MAPPER = {
    "left": (0, -1),
    "up": (-1, 0),
    "main_diagonal": (-1, -1),
    "other_diagonal": (-1, 1),
}

while True:
    player = 2 if turns % 2 == 0 else 1

    try:
        choice = int(input(f"Player {player}, please choose a column (1-{COLS}): "))
        col = choice - 1
        validate_column(col)
        row = get_available_row(col, board)
        board[row][col] = str(player)
        turns += 1

        if winner_found(row, col, board):
            print(f'WINNER IS PLAYER {player}!')
            if choice_to_play_again():
                board = creating_board(ROWS, COLS)
                turns = 1
                pass
            else:
                print("Bye bye, we will miss you!")
                break
        if turns > ROWS * COLS:
            print(f"Board is full nobody wins!")
            if choice_to_play_again():
                board = creating_board(ROWS, COLS)
                turns = 1
                pass
            else:
                print("Bye bye, we will miss you!")
                break

    except FullColumnError:
        print(f"This column is full, please select another one.")
        continue
    except (InvalidColumn, ValueError):
        print(f"This column is invalid, please select a number between 1 and {COLS}!")
        continue

    print_matrix(board)
