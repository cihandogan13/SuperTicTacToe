import numpy as np

class MiniBoard:
    def __init__(self):
        self.Board = np.arange(-9, 0).reshape(3,3)
        self.isResolved = False
        self.winner = -1

    def addMove(self, moveCoordX, moveCoordY, playerId):
        if not self.isResolved and self.Board[moveCoordX, moveCoordY] < 0:
            self.Board[moveCoordX, moveCoordY] = playerId
            return self.checkForWin()
        else: #to do add illegal move check and throw error instead of true false  create status codes
            return True

    def checkForWin(self):
        self.isResolved, self.Winner = self.checkRows()
        if(not self.isResolved):
            self.isResolved, self.Winner = self.checkColumns()
            if(not self.isResolved):
                self.isResolved, self.Winner = self.checkDiagonal()
        return self.isResolved
        

    def checkRows(self):
        winner = -1
        isWin = False
        for index in range(0,3):
            isWin = self.Board[index,0] == self.Board[index,2] and self.Board[index,0] == self.Board[index,1]
            if isWin:
                winner = self.Board[index,0]
                break
        return isWin, winner



    def checkColumns(self):
        winner = -1
        isWin = False
        for index in range(0,3):
            isWin = self.Board[0,index] == self.Board[2, index] and self.Board[0, index] == self.Board[1, index]
            if isWin:
                winner = self.Board[0,index]
                break
        return isWin, winner

    def checkDiagonal(self):
        winner = -1
        isWin = False
        isWin = self.Board[0,0] == self.Board[2, 2] and self.Board[0, 0] == self.Board[1, 1]
        if isWin:
            winner = self.Board[0,0]
            return isWin, winner

        isWin = self.Board[0,2] == self.Board[2, 0] and self.Board[0, 2] == self.Board[1, 1]
        if isWin:
            winner = self.Board[0,2]
        return isWin, winner

    

        
        

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

    