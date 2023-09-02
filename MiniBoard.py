import numpy as np
from Status import Status 

class MiniBoard:
    def __init__(self):
        self.Board = np.arange(-9, 0).reshape(3,3)
        self.isResolved = False

    def addMove(self, moveCoordX, moveCoordY, playerId):
        if self.isResolved or (not self.isResolved and self.Board[moveCoordX, moveCoordY] >= 0):
            return Status.ILLEGAL_MOVE
        elif not self.isResolved and self.Board[moveCoordX, moveCoordY] < 0:
            self.Board[moveCoordX, moveCoordY] = playerId
            
            if self.checkForWin():
                return Status.RESOLVED
            elif all(self.Board.flatten() > 0):
                self.isResolved = True
                return Status.TIE
            else:
                return Status.NOT_RESOLVED
        

    def checkForWin(self):
        self.isResolved = self.checkRows()
        if(not self.isResolved):
            self.isResolved  = self.checkColumns()
            if(not self.isResolved):
                self.isResolved  = self.checkDiagonal()
        return self.isResolved
        

    def checkRows(self):
        isWin = False
        for index in range(0,3):
            isWin = self.Board[index,0] == self.Board[index,2] and self.Board[index,0] == self.Board[index,1]
            if isWin:
                break
        return isWin



    def checkColumns(self):
        isWin = False
        for index in range(0,3):
            isWin = self.Board[0,index] == self.Board[2, index] and self.Board[0, index] == self.Board[1, index]
            if isWin:
                break
        return isWin

    def checkDiagonal(self):
        isWin = False
        isWin = (self.Board[0,0] == self.Board[2, 2] and self.Board[0, 0] == self.Board[1, 1]) or (self.Board[0,2] == self.Board[2, 0] and self.Board[0, 2] == self.Board[1, 1])
        return isWin

    

        
        

# #test
# if __name__=="__main__":
#     for index in range(0,3):
#         board = MiniBoard()
#         
#         print(board.addMove(index,0,1))
#         print(board.Board)
#         print(board.addMove(index,1,1))
#         print(board.Board)
#         print(board.addMove(index,2,1))
#         print(board.Board)
    
#     print("#########################################################")
#     for index in range(0,3):
#         board = MiniBoard()
#         
#         print(board.addMove(0,index,1))
#         print(board.Board)
#         print(board.addMove(1,index,1))
#         print(board.Board)
#         print(board.addMove(2,index,1))
#         print(board.Board)


#     print("#########################################################")
#     board = MiniBoard()
#     
#     print(board.addMove(0,0,1))
#     print(board.Board)
#     print(board.addMove(1,1,1))
#     print(board.Board)
#     print(board.addMove(2,2,1))
#     print(board.Board)

#     print("#########################################################")
#     board = MiniBoard()
#     
#     print(board.addMove(0,2,1))
#     print(board.Board)
#     print(board.addMove(1,1,1))
#     print(board.Board)
#     print(board.addMove(2,0,1))
#     print(board.Board)

    