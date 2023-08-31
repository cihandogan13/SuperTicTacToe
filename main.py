from Board import Board


def getPlayerMove(player, isFirstMove=False):
    message = "Enter Your Move Player" + str(player) + (" X,Y,Z,T:" if isFirstMove else  " Z,T:") 
    print(message)
    move = input()
    coords = move.split(",")
    if isFirstMove and len(coords) == 4:
        return int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]) 
    elif not isFirstMove and len(coords) == 2:
        return int(coords[0]), int(coords[1])
    else:
        return None
    
def addPlayerMove(player, xCoord, yCoord):
    zCoord, tCoord = getPlayerMove(player)
    board.addMove(xCoord, yCoord, zCoord, tCoord,  player)
    return zCoord, tCoord

if __name__=="__main__":
    PLAYER1 = 1
    PLAYER2 = 2
    board = Board()

    board.printBoard()
    #add input check (for now until gui)
    xCoord, yCoord, zCoord, tCoord = getPlayerMove(PLAYER1, isFirstMove=True)
    board.addMove(xCoord, yCoord, zCoord, tCoord,  PLAYER1)

    while(board.winner == -1):
        board.printBoard()
        #add none check
        zCoord, tCoord = addPlayerMove(PLAYER2, zCoord, tCoord)
        zCoord, tCoord = addPlayerMove(PLAYER1, zCoord, tCoord)
