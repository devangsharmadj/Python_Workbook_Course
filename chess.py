class Square:
    # This class represents each square on a chess board
    def __init__(self, letter, integer):
        self.letter = letter
        self.integer = integer

    def ascii_values(self):
        return ord(self.letter)


def main():
    # Getting the square to be checked
    check_square = input('What square needs to be checked: ')
    checker(check_square[0], check_square[1])


def checker(string, integer):
    checking_square = Square(string, integer)
    if (checking_square.ascii_values() + int(checking_square.integer)) % 2 == 0:
        print('Black')
    else:
        print('White')


main()
