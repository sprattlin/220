
"""
Name: <Lindsay Spratt>
<lab9>.py
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    board_index = board[position - 1] # change to string because isnumeric() only works on strings
    str_board_i = str(board_index)
    return str_board_i.isnumeric() # only return because isnumeric() returns a boolean, so it will return t or f

# make sure the spot specified is an empty space
# return true if the move is legal, false if not


def fill_spot(board, position, character):
    character = board[position -1]
    character.split()
    character.lower()
# place the shape at position on the board
# position is not equal to index
# remove whitespace from shape (.strip()) and make sure its lowercase .lower()


def winning_game(board):
    wingame = [[1,2,3]], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9],[3,5,7]
    for condition in wingame:
        count = 0
        for position in condition:
            if board[position] == 'x':
                count += 1
            if count == 3:
                return True
    for condition in wingame:
        count = 0
        for position in condition:
            if board[position] == 'y':
                count += 1
            if count == 3:
                return True
    else:
        return False


def game_over(board):
    if winning_game(board):
        return True
    else:
        return False
# game is over if someone has won or there are no more moves left
# if there are any spaces left and no one has won, then the game is over
# return true if over, false if not


def get_winner(board):
    acc = ''
    for x in board:
        if x == 'x':
            acc += 1

    aoo = ''
    for o in board:
        if o == 'o':
            aoo += 1
    if aoo > acc:
        return 'o'
    if acc > aoo:
        return 'x'

    else:
        return None
# return 'x' if x won, 'o' if o won, none if the game is not over
# if there are more x's than o's, x won, if there are equal x's and o's, o won
# this only works if you make x go first


def play(board):

    board = build_board()
    count = 0

    print_board(board)
    print("Welcome to tic-tac-toe, in order to play, choose a number on the board"
          "to choose your position!")
    while not game_over(board):
        x_spot = eval(input("x where do you want to place your marker?"))

        if is_legal(board, x_spot):
            fill_spot(board, x_spot, 'x')
            count += 1
        print_board(board)

        if game_over(board):
            print(get_winner(board) + 'wins!')
            x = input('Do you want to play again? (yes or no): ')
            if input == x.startswith('y'):
                play(board)
        else:
            print("It's a tie!")
            x = input('Do you want to play again? (yes or no): ')
            if input == x.startswith('y'):
                play(board)


def main(board=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
    play(board)


if __name__ == '__main__':
    main()
