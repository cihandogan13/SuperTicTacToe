from MiniBoard import MiniBoard
from Status import Status
import numpy as np
class Board:
    def __init__(self):
        self.Boards = []
        self.winner = -1
        self.mainGame = np.empty((9, 9), dtype='str')
        self.mainGame[:] = ' '
        for index in range(0,10):
            self.Boards.append(MiniBoard())
        

    def printBoard(self):
        output = ""
        for index in range(0,9):
            for innerIndex in range(0,9):
                output += self.mainGame[index, innerIndex]
                if (innerIndex == 2 or innerIndex==5 ):
                    output += "|"
            output += "\n"
            if (index == 2 or index ==5 ):
                output += "---+---+---\n"
        print(output)
        

    def addMove(self, Xcoord, Ycoord, Zcoord, Tcoord, playerId):
        currentBoard = self.Boards[Xcoord*3 + Ycoord]
        
        result = currentBoard.addMove(Zcoord, Tcoord, playerId)
        #update the main game according to resolution of minigame
        if result == Status.NOT_RESOLVED:
            self.mainGame[Xcoord*3 + Zcoord , Ycoord*3+ Tcoord] = self.getXO(playerId, False)
        elif result == Status.RESOLVED:
            status = self.Boards[9].addMove(Xcoord, Ycoord, playerId)
            self.mainGame[Xcoord*3:(Xcoord+1)*3 , Ycoord*3:(Ycoord+1)*3] = self.getXO(playerId, True)

            if status == Status.RESOLVED:
                self.winner = self.Boards[9].Board[Xcoord, Ycoord] 
                result = Status.FINISHED
            elif status == Status.TIE:
                result = Status.TIE

        elif result == Status.TIE:
            status = self.Boards[9].addMove(Xcoord, Ycoord, 3) #3 for tie
            self.mainGame[Xcoord*3:(Xcoord+1)*3 , Ycoord*3:(Ycoord+1)*3] = self.getXO(-1, True)
            result = Status.RESOLVED

            if status == Status.TIE:
                result = Status.TIE
        return result
    
    def getXO(self, playerId, isBlock):
        if(isBlock):
            dummy = np.empty((3, 3), dtype='str')
            if(playerId == 1):
                dummy= np.array([['\\', ' ', '/'],
                        [' ', 'X', ' '],
                        ['/', ' ', '\\']])
            elif(playerId == 2):
                dummy= np.array([['-', '-', '-'],
                        ['|', ' ', '|'],
                        ['-', '-', '-']])
            elif(playerId == -1):
                dummy= np.array([[' ', ' ', ' '],
                        ['-', '-', '-'],
                        [' ', ' ', ' ']])
            return dummy
        else:
            if(playerId == 1):
                return 'X'
            elif(playerId == 2):
                return 'O'

        
        
        


# #test
if __name__=="__main__":
    board = Board()   
    #X
    print(board.addMove(0,0,0,0,1))
    print(board.addMove(0,0,0,1,1))
    print(board.addMove(0,0,0,2,1))
    board.printBoard()
    #O
    print(board.addMove(1,1,0,0,2))
    print(board.addMove(1,1,0,1,2))
    print(board.addMove(1,1,0,2,2))
    board.printBoard()

    #TIE
    print(board.addMove(2,2,0,0,1))
    print(board.addMove(2,2,0,1,1))
    print(board.addMove(2,2,0,2,2))
    print(board.addMove(2,2,1,0,2))
    print(board.addMove(2,2,1,1,2))
    print(board.addMove(2,2,1,2,1))
    print(board.addMove(2,2,2,0,1))
    print(board.addMove(2,2,2,1,1))
    print(board.addMove(2,2,2,2,2))
    board.printBoard()


    #print(len(board.Boards))