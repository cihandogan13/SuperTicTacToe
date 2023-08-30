from MiniBoard import MiniBoard
class Board:
    def __init__(self):
        self.Boards = []
        self.winner = -1
        for index in range(0,10):
            self.Boards.append(MiniBoard())

    def printBoard(self):
        for board in self.Boards:
            print(board.Board)
        

    def addMove(self, Xcoord, Ycoord, Zcoord, Tcoord, playerId):
        currentBoard = self.Boards[Xcoord*3 + Ycoord]
        if not currentBoard.isResolved:
            result = currentBoard.addMove(Zcoord, Tcoord, playerId)
            #update the main game according to resolution of minigame
            if result:
                if(self.Boards[9].addMove(Xcoord, Ycoord, playerId)):
                    self.winner = True # add a function that checks if the games is finished after every move
                #check after this if the game is finished or not
            return result
        else:
            return None # return None so that game won't let you the play resolved minigame


# #test
if __name__=="__main__":
    board = Board()   
    print(board.addMove(0,0,0,0,1))
    board.printBoard()
    print(len(board.Boards))
    print("##############")
    print(board.addMove(0,0,0,1,1))
    board.printBoard()
    print("##############")
    print(board.addMove(0,0,0,2,1))
    board.printBoard()
    print("##############")

    print(len(board.Boards))