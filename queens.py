from select import select
from tabnanny import check


class Queens(object):
    #initialize a chess board


    def __init__(self, n=8):
        self.board = []
        self.n = n
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)

        
    def print_board(self):
        for i in range (self.n):
            for j in range (self.n):
                print(self.board[i][j], end=' ')
            print()
        print()



    # check if no queen captures another queen at that location
    def is_valid(self, row, col):
        for i in range(self.n):
            if (self.board[row][i]=='Q') or (self.board[i][col]=='Q'):
                return False
        
        for i in range (self.n):
            for j in range(self.n):
                row_diff = abs(row-i)
                col_dif = abs(col - j)
                if(row_diff==col_dif) and (self.board[i][j]=='Q'):
                    return False

        return True

    # do a recursive backtracking
    def recursive_solve(self,col):
        
        if(col==self.n):
            return True
        else:
            for i  in range(self.n):
                if(self.is_valid(i,col)):
                    self.board[i][col] = 'Q'
                    if(self.recursive_solve(col+1)):
                        return True

                    self.board[i][col] = '*'
                return False
                    

    # if the problem has a solution, print the board
    def solve(self):
        for i in range(self.n):
            if(self.recursive_solve(i)):
                self.print_board()

def main():
    # create a chess board
    game = Queens(13)

    #place the queens on the board
    game.solve()


main()



        