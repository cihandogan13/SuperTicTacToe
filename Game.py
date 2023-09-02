from Board import Board
from Status import Status


class Game:
    def __init__(self):
        self.board = Board()
        self.lastMoveStatus = Status.FIRST_MOVE
        self.winner = -1
        self.currentPlayer = 0

    def isPlayerFree(self):
        if (self.lastMoveStatus == Status.FIRST_MOVE) or (self.lastMoveStatus == Status.RESOLVED):
            return True
        else:
            return False
        
    def getPlayerMove(self):
        message = "Enter Your Move Player" + str(self.currentPlayer + 1) + (" X,Y,Z,T:" if self.isPlayerFree() else  " Z,T:") 
        print(message)

        move = input()
        coords = move.split(",")

        if self.isPlayerFree()  and len(coords) == 4:
            return int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]) 
        elif not self.isPlayerFree() and len(coords) == 2:
            return int(coords[0]), int(coords[1])
        else:
            print("Wrong Input!")
            return self.getPlayerMove() #go recursive until you get right input looks better than do-while?
    
    def addPlayerMove(self, xCoord, yCoord):
        if self.isPlayerFree():
            xCoord, yCoord, zCoord, tCoord = self.getPlayerMove()
        else:
            zCoord, tCoord = self.getPlayerMove()
        self.lastMoveStatus = self.board.addMove(xCoord, yCoord, zCoord, tCoord, self.currentPlayer + 1)
        if self.lastMoveStatus == Status.ILLEGAL_MOVE:
            print("Illegal Move! Play Again!")
            zCoord, tCoord = self.addPlayerMove(xCoord,yCoord) #go recursive until you get legal move looks better than do-while?
        return zCoord, tCoord
    
    def play(self):
        #add input check (for now until gui)
        zCoord, tCoord = None, None
        while(self.lastMoveStatus != Status.FINISHED): #to do last game status check
            self.board.printBoard()
            zCoord, tCoord = self.addPlayerMove( zCoord, tCoord)
            self.currentPlayer = (self.currentPlayer + 1) % 2
        self.winner = self.board.winner
        print(self.winner)