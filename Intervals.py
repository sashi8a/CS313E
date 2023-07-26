#  File: Intervals.py

#  Description: The aim in this assignment is take a set of intervals and collapse all the overlapping intervals and print the smallest set of non-intersecting intervals in ascending 
# order of the lower end of the interval and then print the intervals in increasing order of the size of the interval.

#  Student Name: Sashi Ayyalasomayajula

#  Student UT EID: sa55465

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 9/6/22

#  Date Last Modified: 9/9/22
import sys
import math
from tracemalloc import start

# Input: tuples_list is an unsorted list of tuples denoting intervals

# Output: a list of merged tuples sorted by the lower number of the
# interval
def merge_tuples(tuples_list):


    tuples_list = sorted(tuples_list)

    endings = []
    startings = []

    min = 0 #sets placeholder for min value
    max = 0 #sets placeholder for max value

    #loops through tuples_list and sets min and max to 
    # the absolute min and max numbers in all of the intervals in tuples_list
    # records the starting and ending vlaues  of the tuples into arrays
    for i in range(len(tuples_list)): 

        endings.append(tuples_list[i][1])
        startings.append(tuples_list[i][0])
                                      

        x = tuples_list[i]

        if x[0]<min:
            min = x[0]

        if x[1]>max:
            max = x[1]

    #creates an array the length of the range from min to max
    # and fills all elements with value False
    bool_arr = [False]*((max-min)+1)


    #creates an empty list meant to store the indexes of intervals where the
    #  end intger is exactly one less than the start of the next interval
    consec_int = [] 



    # loops through tuples_list
    for tup in tuples_list:

        for j in range((tup[0]-min), (tup[1]-min)+1): #goes through the bool_arr's index's relative to all the values within the tuples in tup_list
            
            bool_arr[j] = True #sets the False in the element to true

    for x in range(1, len(bool_arr)):

        consec = True #initially sets consec to True at the beginning of each loop

        for n in range(len(tuples_list)): 

            if (tuples_list[n][0]< (x-1)+min) and (tuples_list[n][1]> (x+min)): # checks if the first element in the tuple is less than the previous integers value  and greater for the second element

                consec = False # if so, sets consec to false


        if (consec) and (x+min in startings) and (x-1+min in endings): #checks if consec is true and that the current and previous integers are in starting and ending, respectively
            consec_int.append(x) 



    merged_arr = [] #create empty tuple array
    dummy_tuple = (None,None) #place holder tuple

    #loops through length of bool_arr
    for i in range(len(bool_arr)):

        #conditional that checks if first element of dummy tuple is none and if bool_arr at i reads True
        if dummy_tuple[0] == None and bool_arr[i]:

            dummy_tuple = (i + min,None) #sets the first index of dummy tuple as the index of bool_arr where it is true ands adds the minimum value to convert it

        # checks if dummy tuple is not none but the second element of dummy tuple IS none, and bool_arr at i is False.
        elif dummy_tuple[0] is not None and dummy_tuple[1] is None and not bool_arr[i]:
            dummy_tuple = (dummy_tuple[0], (i - 1) + min ) # ends interval
            merged_arr.append(dummy_tuple) # adds interval to merged list
            dummy_tuple = (None, None) #resets dummy_tuple

        # if the index i is contained in the list consec_int
        elif i in consec_int:
            dummy_tuple = (dummy_tuple[0], (i - 1) + min )  #ends the tuple at the elemment one before the current index
            merged_arr.append(dummy_tuple) # appends interval
            dummy_tuple = (i + min, None)  # resets dummy tuple

        
        # checks if i is at the last term in bool_arr
        elif i == len(bool_arr)-1: 
            dummy_tuple = (dummy_tuple[0], i + min) #resets dummy_tuple
            merged_arr.append(dummy_tuple) # appends dummy_tuple to merged_arr


    return sorted(merged_arr) #returns sorted merged_arr



# Input: tuples_list is a list of tuples denoting intervals

# Output: a list of tuples sorted by ascending order of the size of
# the interval if two intervals have the size then it will sort by the
# lower number in the interval
def sort_by_interval_size(tuples_list):

    sorted_list = []    #creates empty list to store sorted intervals

    tuplesize_dict = {} #creates empty dictionary to connect each tuple to its respective length

    for tup in tuples_list:
        tuplesize_dict.update({tup:(tup[1]-tup[0])}) #fills dictionary

    dict_pair_list = tuplesize_dict.items() #creates a filed list of tuples with the elements being (tuple,tuple size)


    # loop which finds the minimum length of all the tuples in tuples_list
    min = sys.maxsize
    for pair in dict_pair_list:

        if pair[1]<min:
            min = pair[1]
    

    # variable to track ascending length of intervals
    counter = min

    # loop which appends each tuple to sorted_list in ascending order 
    while len(sorted_list)!=len(tuples_list):
        for d in dict_pair_list:
            if d[1]== counter:
                sorted_list.append(d[0])
        
        counter+=1

    return sorted_list

    
# Input: no input

# # Output: a string denoting all test cases have passed
# def test_cases ():
#   assert merge_tuples([(1,2)]) == [(1,2)]
#   assert merge_tuples([(1,4),(2,3),(3,10)]) == [(1,10)]
#   assert merge_tuples([(1,2), (3,4), (5,7),(6,13)]) == [(1,2), (3,4), (5,13)]

#   assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
#   assert sort_by_interval_size([(1,3), (4,8)]) == [(1,3), (4,8)]
#   assert sort_by_interval_size([(6,10), (25,29), (4,8), (35,36)]) == [(35,36),(4,8),(6,10),(25,29)]




#   return "all test cases passed"
# test_cases ()         

def main():


    #reads input file
    f = open('intervals.in', 'r').readlines()


    #sets n to first line of input which is used 
    # to loop through the number of intervals in input
    n = int(f[0].strip())


    
    #creates empty list to store tuples from input
    tup_list = []


    #swifts through input file and adds each tuple to tup_list
    for i in range(1,n+1):
        x = f[i].split(' ')
        tup_list.append((int(x[0]), int(x[1])))

    
    my_merged_list = merge_tuples(tup_list)

    print(my_merged_list)

    print(sort_by_interval_size(my_merged_list))
main()