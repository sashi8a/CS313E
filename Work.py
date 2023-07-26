#  File: Work.py 

#  Description:  

#  Student Name: Sashi Ayyalasomayajula

#  Student UT EID: sa55465

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 9/28/22

#  Date Last Modified: 9/28/22

import sys, time

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
  # use linear search here

  v = 0 #sets initial value of v to zero as place holder

  for i in range(1,n): # loops through all values from 1 to number of lines to code
        if(find_sum(i,k)>=n): # calls find_sum function for each value

            v = i #if v value works, resets v and breaks loop
            break


  if n<10: #if n is less than 10 returns n as optimal v, else returns v from loop
      return n
  else:
      return v 



#input: int v, int k, representing a theoretical starting value v with productivity factor k
#output: an int representing the number of lines of code written using this combination of v and k
def find_sum(v, k):

    total = v #total starts at v because user has already written v lines before drinking first coffee
    pwr = 1
    const = k

    while (v//k**pwr)>0:   #while condition which checks whether user has "fallen asleep"
        total += v//k**pwr
        pwr+=1
    
    return total



# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
  # use binary search here

  # sets initial markers of low,high.middle, and productivity factor
  low = 1 
  high = n
  middle = (low+high)//2 
  pwr = k

  

  while(middle!=low): #checks if the values of low and middle are unequal
        if(find_sum(middle,pwr)<n): #resets low to current middle if v value doesnt allow user to finish n lines of code
            low = middle
        elif(find_sum(middle,pwr)>=n): # resets high value to middle if v value equaled or exceed n lines of code
            high = middle

        middle = (low+high)//2 # resets middle according to the new high or low

  if(find_sum(middle,pwr))<n: #checks for edge case where optimal v is middle in while loop. If so, increments middle by one.
    middle+=1

  if n<10: # returns n if less than 10 because it would be the optimal v
      return n
  else:
      return middle # else, returns middle


# main has been completed for you
# do NOT change anything below this line
def main():
  num_cases = int((sys.stdin.readline()).strip())

  for i in range(num_cases):
        inp = (sys.stdin.readline()).split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()