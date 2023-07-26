
#  File: Boxes.py

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

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes(box_list):

    n = len(box_list)  #num of boxes
    
    N_i = [0 for i in range (n)] #fills nest_level list with temp zeros
    R_i = [0 for j in range (n)]#fills R_i list with temp zeros

    for i in range(0, n): # outer for loop goes through all of the boxes in increasing order of the singular dimension



        j = i - 1 #sets j as a relative variable as the previous index at every i
        curr_max = 0

        while j >= 0: 

            temp_nest = N_i[j]

            if does_fit(box_list[j], box_list[i]): #while j is a box in boxlist, if box at j fits in the box at i, sets the nest level equal to temp nest
                nest_level = temp_nest

                if nest_level >= curr_max: #sets curr_max to the local highest nest level 

                    curr_max = nest_level

            j -= 1

        x = i - 1 #sets x as a relative variable as the previous index at every i
        while x >= 0:

            curr_nest_level = N_i[x]
            temp = curr_max

            if does_fit(box_list[x], box_list[i]): # while box list at x exists, if it fits in box list at i, add the index to R_i if if condition is met

                if curr_nest_level == temp:

                    R_i[i] += R_i[x]

            x -= 1

        N_i[i] = (curr_max+1) #resets current value of nest level at i

        if R_i[i] == 0: #if there are no boxes that fit into the current, change R_i at the index from zero to one to account for the box.
            R_i[i] = 1

    N = len(N_i)
    R = len(R_i)
    highest_nest = max(N_i) # finds value of the largest box that can nest the highest number of smaller boxes,
    num_sets = 0 #place holder
    

    for i in range(R): #goes through R_i

        if N_i[i] == highest_nest: #adds R_i to numsets if the current nest value equals the max nest value
            num_sets += R_i[i]

    return highest_nest, num_sets

# returns True if box1 fits inside box2
def does_fit (box1, box2):
    return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
    # read the number of boxes 
    line = sys.stdin.readline()
    line = line.strip()
    num_boxes = int (line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range (num_boxes):
        line = sys.stdin.readline()
        line = line.strip()
        box = line.split()
        for j in range (len(box)):
            box[j] = int (box[j])
        box.sort()
        box_list.append (box)

    # print to make sure that the input was read in correctly
    #print (box_list)
    print()

    # sort the box list
    box_list.sort()

    # print the box_list to see if it has been sorted.
    #print (box_list)
    print()

    # get the maximum number of nesting boxes and the
    # number of sets that have that maximum number of boxes
    max_boxes, num_sets = nesting_boxes (box_list)

    # print the largest number of boxes that fit
    print (max_boxes)

    # print the number of sets of such boxes
    print (num_sets)

if __name__ == "__main__":
    main()
