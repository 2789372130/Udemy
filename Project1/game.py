# import tkinter.messagebox

class Board:
    """
    A class to represent the game board for tic tac toe.

    ...

    Attributes
    ----------
    row1 : list of chars
        first row of game board
    row2 : list of chars
        second row of game board
    row3 : list of chars
        third row of game board

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """

    current_player = 'O'

    def __init__(self, player_number, row1, row2, row3):
        self.player_number = player_number
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
        pass

    def __str__(self):
        '''
        Print the current game board
        '''
        return f"{self.row1[0]} | {self.row1[1]} | {self.row1[2]}\n" +\
            f"{self.row2[0]} | {self.row2[1]} | {self.row2[2]}\n" +\
            f"{self.row3[0]} | {self.row3[1]} | {self.row3[2]}\n"
        # return f"{self.row1}\n{self.row2}\n{self.row3}"

    def change_player(self):
        if self.current_player == 'O':
            self.current_player = 'X'
        else:
            self.current_player = 'O'
        pass

    def input_location(self, row, column):
        cp = self.current_player
        if row == 1:
            self.row1[column-1] = cp
        elif row == 2:
            self.row2[column-1] = cp
        else:
            self.row3[column-1] = cp
        pass

    def print_game_state(self):
        return self.current_player +\
            "".join(map(str, self.row1)) +\
            "".join(map(str, self.row2)) +\
            "".join(map(str, self.row3))

    def end_state(self):
        '''
        Check if the current game has a winner and declear the winner

            Parameters: 
                None

            Return:
                (char): 'O' if 'O' wins
                        'X' if 'X' wins
                        'n' if there is no winner
        '''
        gs = self.print_game_state()
        if gs[1] == gs[2] == gs[3]:
            if gs[1] == 'O':
                return 'O'
            elif gs[1] == 'X':
                return 'X'
        elif gs[4] == gs[5] == gs[6]:
            if gs[4] == 'O':
                return 'O'
            elif gs[4] == 'X':
                return 'X'
        elif gs[7] == gs[8] == gs[9]:
            if gs[7] == 'O':
                return 'O'
            elif gs[7] == 'X':
                return 'X'
        elif gs[1] == gs[5] == gs[9]:
            if gs[1] == 'O':
                return 'O'
            elif gs[1] == 'X':
                return 'X'
        elif gs[3] == gs[5] == gs[7]:
            if gs[3] == 'O':
                return 'O'
            elif gs[3] == 'X':
                return 'X'
        elif gs[1] == gs[4] == gs[7]:
            if gs[1] == 'O':
                return 'O'
            elif gs[1] == 'X':
                return 'X'
        elif gs[2] == gs[5] == gs[8]:
            if gs[2] == 'O':
                return 'O'
            elif gs[2] == 'X':
                return 'X'
        elif gs[3] == gs[6] == gs[9]:
            if gs[3] == 'O':
                return 'O'
            elif gs[3] == 'X':
                return 'X'
        return 'n'

# INIT_STATE = False


def init_board(player_number):
    '''
    Create an empty board
    '''
    # if INIT_STATE: pass
    row = ['*', '*', '*']
    row2 = ['O', 'X', 'O']
    game_board = Board(player_number, row, row.copy(), row.copy())
    # INIT_STATE = True
    return game_board


def detect_input(game_board):
    '''
    Recieve user inputs and return the valid pair
    '''
    validation = True
    while validation:
        row = input("Please first enter the row number(1-3)")
        column = input("Please then enter the column number(1-3)")
        if not validate_input(game_board, int(row), int(column)):
            # tkinter.messagebox.showwarning(title="Error", message="Invalid input(s)")
            input("Invalid input(s), press Enter to redo")
        else:
            validation = False
    return int(row), int(column)


def validate_input(game_board, row, column):
    '''
    Check if the inputs are valid

        Parameters:
            row(int): Row number
            column(int): Column number

        Return:
            (boolean): Whether the inputs are valid or not
        '''
    gs = game_board.print_game_state()
    if type(row) != int or type(column) != int:
        return False
    if row > 0 and row < 4 and column > 0 and column < 4:
        if gs[column + 3 * (row - 1)] == '*':
            return True
    return False


# game_board = Board([1, 2, 3], [" ", " ", " "], [" ", " ", " "])
# print(game_board)
# a, b = game_board.detect_input()
# game_board.validate_input(a, b)

# gb = init_board(2)
# print(gb)
# print(gb.print_game_state())
# print(gb.end_state())
# gb.change_player()
# print(gb.print_game_state())


# gb = init_board(2)
# print(gb)
# gb.input_location(2, 2)
# gb.change_player()
# print(gb.print_game_state())
# print(gb)
# gb.input_location(1, 3)
# gb.change_player()
# print(gb.print_game_state())
# print(gb)
# gb.input_location(3, 1)
# gb.change_player()
# print(gb.print_game_state())
# print(gb)
# gb.input_location(2, 1)
# gb.change_player()
# print(gb.print_game_state())
# print(gb)
# gb.input_location(3, 2)
# gb.change_player()
# print(gb.print_game_state())
# print(gb)
# gb.input_location(1, 1)
# gb.change_player()
# print(gb.print_game_state())
# print(gb)
# gb.input_location(1, 2)
# gb.change_player()
# print(gb.print_game_state())

gb = init_board(2)
while gb.end_state() == 'n' and gb.print_game_state().find('*') != -1:
    print(f"\n The current player is {gb.current_player}, please make your move.")
    print("The current board is:")
    print(gb)
    row, column = detect_input(gb)
    gb.input_location(row, column)
    gb.change_player()
gb.change_player()
if gb.print_game_state().find('*') == -1:
    print(f"Congratulations player {gb.current_player}")
else:
    print(f"It's a draw!")
