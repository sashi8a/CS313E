
#  File: Triangle.py

#  Description:

#  Student Name: Sashi Ayyalasomayajula

#  Student UT EID: sa55465

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force (grid):

  sums = [] #creates empty list to store all sums
  brute_force_helper(grid,sums, 0,0,0) #calls helper starting at row and col zero and total being zero.
  final = max(sums) 

  return final #prints out max sum path


# helper function which takes in the grid, a list of sums, integers for row and column , and total value
def brute_force_helper(grid, sums, i , j, total): 
  total+=grid[i][j] #initially adds current node total
  if i == len(grid)-1: #if last line of triangle is reached, appends the total sum for that path to sums
     sums.append(total)
  else: # else, recalls helper function with the node directly below the current node and the node below and to to the right (the next two possible path directions)
     brute_force_helper(grid, sums, i+1, j, total)  
     brute_force_helper(grid, sums, i+1, j+1, total)


  



# returns the greatest path sum using greedy approach
def greedy (grid):

  total = grid[0][0] #starts total sum value with top value of trianlge

  curr_index = 0
  i = 1
  adjacent_values = []
  prev_value = grid[0][0]
  current_value_colindex = 0
  prev_colindex = 0

  while(i<len(grid)):
      next_row = grid[i] #looks only at next row in triangle

      if grid[curr_index].index(prev_value)>=prev_colindex: #checks if index of previous value is greater than or equal to the current value
         current_value_colindex = grid[curr_index].index(prev_value) #if so, sets current value colindex to the index of previous value
      else:
         temp_arr = grid[curr_index][:] #if this isnt true, it means there is a repeat number, and so the list is split at the repeat and a new value for current value colindex is set.
         current_value_colindex = temp_arr[grid[curr_index].index(prev_value)+1:].index(prev_value) + 1 + (grid[curr_index].index(prev_value)+1) 
      #appends the two paths to the adjacent values list
      adjacent_values.append(next_row[current_value_colindex])
      adjacent_values.append(next_row[current_value_colindex+1])


      prev_colindex = current_value_colindex

      prev_value = max(adjacent_values) #resets prev value to the max of the possible paths

      #increments all interator variables
      total+= prev_value
      i+=1
      curr_index+=1
      adjacent_values.clear()  #clear adjacent values for next iteration of while loop

  return total



# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
  return divide_conquer_helper(grid,0,0)


def divide_conquer_helper(grid,i,j):

  curr_value = 0 #place holder value
  if (i==len(grid)-1) and (j==len(grid[i])-1): #if the current value is at the bottom right of the triangle, return it.
     return grid[i][j]
  elif (i==len(grid)-1) and (j!=len(grid[i])-1): #if on the last line of the triangle but not the bottom right, return the greater value between the two possible paths
     vals = []
     vals.append(grid[i][j])
     vals.append(grid[i][j+1])
     return max(vals)
  else:  #if not on the last line, return the current value added to the max value of helper funciton with the next two posisble paths.
     curr_value = grid[i][j]
     return curr_value + max( divide_conquer_helper(grid,i+1,j), divide_conquer_helper(grid, i+1, j+1))

     


  

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  # print_grid(copy)
  max_line = len(grid) - 1

  for i in range(len(grid) - 1, 0, -1): #loops through trianlge starting from last line
      for j in range(max_line): # goes through each value of last line
          maximum = max(grid[i][j], grid[i][j + 1]) #sets maximum as the larger value between two adjacent values
          grid[i - 1][j] += maximum #adds the maximum value to the element in the line above the current line at the same column index.
      max_line -= 1 
  return grid[0][0] #returns the first element of the array, which is the final sum

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  '''
  # check that the grid was read in properly
  print (grid)
  '''

  print(brute_force(grid))
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search


  print(greedy(grid))
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach

  print(divide_conquer(grid))
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach

  print(dynamic_prog(grid))
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming

if __name__ == "__main__":
  main()