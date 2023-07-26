#  File: Spiral.py

#  Description: Creates a spiral of incresaing integers into NxN square (N%2!=0), finds sums of adjacent numbers 
#               around a specific input value if applicable

#  Student Name: Sashi Ayyalasomayajula

#  Student UT EID: sa55465

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS313E

#  Unique Number: 52535

#  Date Created: 8/29/22

#  Date Last Modified: 9/2/22

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0

import sys
import math

# beginning of create spiral function
def create_spiral(n):

    #reads first line of input and sets square dimensions

    rows, cols = (n,n)


    #place markers for middle of the square
    mid_r = rows//2
    mid_c = cols//2

    #creates inital empty spiral
    spiral = []
    for i in range(rows):
        temp = []
        for j in range(cols):
            temp.append(0)
        spiral.append(temp)



    #sets the absolute midpoint of the square as 1 (applies to all created spirals)
    spiral[mid_r][mid_c] = 1

    #counter acts as the next number to be placed in the 2D list
    counter = 2

    #number of spaces travelled in the same direction
    dist = 1

    #sets the direction to be travelled in
    direction = 'E'

    #place holders for the current position in the 2D list
    current_row = mid_r
    current_col = mid_c

    #counts how many steps taken in a particular direction
    runner=0
    direction_tracker = 0

    #start of while loop to fill in the 2D list
    while counter <= n*n:

        #conditonal statement if direction is east
        if direction == 'E':

            #loops how many ever steps dist is at the current time
            for i in range(dist):

                # checks if the direct right space exists
                if current_col+1<=cols-1:
                    spiral[current_row][current_col+1]=counter
                    runner+=1
                    direction_tracker+=1
                    counter+=1
                    current_col+=1

        
            
            if direction_tracker//dist==1:
                direction = 'S'
                direction_tracker = 0

            if runner//dist==2:
                dist+=1
                runner = 0

                

        #conditonal statement if direction is south
        if direction == 'S':


            for i in range(dist):

                # checks if the direct downward space exists
                if current_row+1<=rows-1:

                    #sets next position in spiral
                    spiral[current_row+1][current_col]=counter
                    #increments counter, runner, and distance tracker
                    runner+=1
                    direction_tracker+=1
                    counter+=1
                    #redfines current position
                    current_row+=1

            #conditional statement to check whether or not to change direction
            if direction_tracker//dist==1:
                direction = 'W'
                direction_tracker = 0

            #conditional statement to check whether or not to increase number of steps in a particular direction
            if runner//dist==2:
                dist+=1
                runner = 0



        #conditonal statement if direction is west
        if direction == 'W':


                for i in range(dist):

                    # checks if the direct left space exists
                    if current_col-1>=0:


                        spiral[current_row][current_col-1]=counter
                        runner+=1
                        direction_tracker+=1
                        counter+=1
                        current_col-=1

                if direction_tracker//dist==1:
                    direction = 'N'
                    direction_tracker = 0

                if runner//dist==2:
                    dist+=1
                    runner = 0

    
        #conditonal statement if direction is North
        if direction == 'N':


                for i in range(dist):

                    #checks if direct upward space exists
                    if current_row-1>=0:


                        spiral[current_row-1][current_col]=counter
                        runner+=1
                        direction_tracker+=1
                        counter+=1
                        current_row-=1

                if direction_tracker//dist==1:
                    direction = 'E'
                    direction_tracker = 0

                if runner//dist==2:
                    dist+=1
                    runner = 0

    #outputs filled spiral
    return spiral 

# ending of create spiral funciton


# beginning of sum of adjacent numbers function
def sum_adjacent_numbers (spiral, n):

    #sets initial sum to zero
    sum = 0

    # boolean value to determine whether or not n is in spiral
    key = False
    
    #sets initial positions of row and col
    start_row = 0
    start_col = 0

    #sets total number of rows and cols in spiral
    rows = len(spiral)
    cols = len(spiral[0])

    #determines whether or not n is in spiral. If yes, key is true .
    for c in range(rows):
        for d in range(cols):
            if spiral[c][d] == n:
                key = True
                start_row = c
                start_col = d


    #adds value to the north of start point
    if start_row-1>=0:
        sum+= spiral[start_row-1][start_col]
        
    #adds value north-east of start point
    if (start_row-1>=0) and (start_col+1<=cols-1):
        sum+= spiral[start_row-1][start_col+1]
            

    #adds value to the east of start point
    if start_col+1<=cols-1:
        sum+=spiral[start_row][start_col +1]

    #adds value south east of start point
    if (start_row+1<=rows-1) and (start_col+1<=cols-1):
        sum+= spiral[start_row+1][start_col+1]

    #adds value south of start point
    if start_row+1<=rows-1:
        sum+=spiral[start_row+1][start_col]

    #adds valus south west of start point
    if (start_row+1<=rows-1) and (start_col-1>=0):
        sum+= spiral[start_row+1][start_col-1]

    #adds value west of start point
    if start_col-1>=0:
        sum+=spiral[start_row][start_col-1]

    #adds value north west of start point
    if (start_row-1>=0) and (start_col-1>=0):
        sum+=spiral[start_row-1][start_col-1]


    # conditional statement that prints out the sum if n is in spiral, and prints out 0 otherwise
    if key:
        print(sum)
    else:
        print('0')






def main():

    #reads input file
    f = open('spiral.in', 'r').readlines()

    #sets n to first line of input
    n = int(f[0].strip())

    #calls create_spiral funciton, using n as the parameter
    my_spiral = create_spiral(n)

    #swifts through input file and prints out sums
    for i in range(1,len(f)):
        x = int(f[i].strip())
        sum_adjacent_numbers(my_spiral,x)
main()



        



    



