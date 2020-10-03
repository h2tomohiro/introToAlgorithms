theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

def printBoard(board):
    print('  ' + board['1'] + '|' + '  ' + board['2'] + '|' + board['3'])
    print('---' + '|' + '---' + '|' + '---')
    print('  ' + board['4'] + '|' + '  ' + board['5'] + '|' + board['6'])
    print('---' + '|' + '---' + '|' + '---')
    print('  ' + board['7'] + '|' + '  ' + board['8'] + '|' + board['9'])

def game():
    turn = 'X'
    count = 0
    print("Tic-Tac-Toe! \nPlayer1 is 0 and Player2 is X.")
    printBoard(theBoard)

    for i in range(10):
        print("Please make your move![1-9]:")
        move = input()

        try:
            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
                printBoard(theBoard)

            else:
                print("Invalid move! Please try again!:")
                continue

            if count >= 5:
                if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                    print("Congratulations " + turn + " won!")
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                    print("Congratulations " + turn + " won!")
                    break
                elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                    print("Congratulations " + turn + " won!")
                    break
                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                    print("Congratulations " + turn + " won!")
                    break
                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                    print("Congratulations " + turn + " won!")
                    break
                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                    print("Congratulations " + turn + " won!")
                    break
                elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                    print("Congratulations " + turn + " won!")
                    break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                    print("Congratulations " + turn + " won!")
                    break

            if count == 9:
                print("It's a draw!")

            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

        except KeyError:
            print("Invalid Input! Please enter a number!: ")

if __name__ == "__main__":
    game()
