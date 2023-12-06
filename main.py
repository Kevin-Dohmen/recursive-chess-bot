
# pieces = ["pawn", "knight", "bishop", "rook", "queen", "king"]
pieces = [[*"pkbrqk"], [*"PKBRQK"]]
print(pieces)
startSetup = [
    [3, 1, 2, 4, 5, 2, 1, 3],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [13, 11, 12, 14, 15, 12, 11, 13]
]

board = startSetup


def renderBoard(board):
    boardStr = "+----------------+\n"
    for y in range(len(board)):
        lineString = "|"
        for x in range(len(board[y])):
            piece = board[y][x]
            print(piece)
            
            if piece < 6:
                lineString += pieces[0][piece]*2
            elif piece >= 10:
                lineString += pieces[1][piece-10]*2
            elif (y + x) % 2 == 0:
                lineString += "  "
            else:
                lineString += "##"
        boardStr += lineString + "|\n"
        
    boardStr += "+----------------+"
    print(boardStr)


def main():
    print("haaayyy")
    renderBoard(board)
    

main()