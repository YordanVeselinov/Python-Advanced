from collections import deque


class InvalidAnswerForPlayAgain(Exception):
    pass


def play_again():
    print("Do you want to play again?")
    while True:
        try:
            choice = input("Please select Yes or No ( Y or N ): ").lower()

            if choice in ["y", "n"]:
                if choice == "y":
                    start_game()
                else:
                    print('Goodbye we will miss you.')
                    raise SystemExit
            else:
                raise InvalidAnswerForPlayAgain

        except InvalidAnswerForPlayAgain:
            print("Invalid answer please select Y or N!")


def check_for_win():
    player_name, player_symbol = players[0].values()

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(SIZE)])
    second_diagonal_win = all([board[i][SIZE - i - 1] == player_symbol for i in range(SIZE)])

    row_win = any([all([el == player_symbol for el in row]) for row in board])
    col_win = any([all([board[r][c] == player_symbol for r in range(SIZE)]) for c in range(SIZE)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print_board()
        print(f"{player_name} won!")
        play_again()




def choose_position():
    global turns

    while True:
        try:
            position = int(input(f"{players[0]['name']} choose a free position [1-{SIZE * SIZE}]: "))
            row, col = (position - 1) // SIZE, (position - 1) % SIZE
        except ValueError:
            print_select_a_valid_position_message()
            continue

        if 1 <= position <= SIZE * SIZE and board[row][col] == " ":
            turns += 1
            place_symbol(row, col)
        else:
            print_select_a_valid_position_message()


def place_symbol(row, col):
    board[row][col] = players[0]["symbol"]

    check_for_win()
    print_board()

    if turns == SIZE * SIZE:
        print("Draw!")
        play_again()

    players.rotate()


def print_select_a_valid_position_message():
    print(f"{players[0]['name']}, please select a valid position!")


def print_game_state():
    print("This is the numeration of the board: ")
    print_board()
    print("--- Good luck! ---")

    for row in range(SIZE):
        for col in range(SIZE):
            board[row][col] = " "


def print_board():
    [print(f"| {' | '.join(row)} |") for row in board]


def start_game():
    player_one = input("Player one enter your name: ")
    player_two = input("Player two enter your name: ")

    while True:
        player_one_symbol = input(f"{player_one} would you like to play with 'X' or 'O'? ").upper()

        if player_one_symbol not in ["O", "X"]:
            print(f"{player_one}, please select a valid option!")
            continue
        else:
            break

    player_two_symbol = 'O' if player_one_symbol == "X" else "X"

    players.append({"name": player_one, "symbol": player_one_symbol})
    players.append({"name": player_two, "symbol": player_two_symbol})

    print_game_state()
    choose_position()


turns = 0
SIZE = 3

print(f" --- Welcome to my console Tic Tac Toe game --- ")

board = [[str(r + c) for c in range(SIZE)] for r in range(1, SIZE * SIZE + 1, SIZE)]
players = deque()

start_game()
