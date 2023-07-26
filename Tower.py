#  File: Tower.py

#  Description:

#  Student's Name: Sashi Ayyalasomayajula

#  Student's UT EID: sa55465

#  Partner's Name: N/A

#  Partner's UT EID: N/A

#  Course Name: CS 313E 

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys
import math

# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves(n):
    #Base case, less than 2 disks, return original hanoi formula as we don't use extra rod
    if n <= 2:
        return 2 ** n - 1
    else:
        k = int(n - math.sqrt(2 * n + 1) + 1)
        moves = 2 * num_moves(k) #multiplying by two takes into account the inital moving of k disks from source to spare 1, then from spare1 to dest.

        # small enough value for original hanoi problem using only 3 pegs instead of 4
        moves += 2 * (2 ** (n-k-1) - 1) #multiplying by two takes into account the inital moving of n-k-1 disks from source to spare 2, then from spare2 to dest.
        moves += 1
        return moves

def main():
  # read number of disks and print number of moves
    for line in sys.stdin:
        line = line.strip()
        num_disks = int (line)
        print (num_moves (num_disks))

if __name__ == "__main__":
    main()
