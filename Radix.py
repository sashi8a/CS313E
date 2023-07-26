
#  File: Radix.py

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

class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return (self.queue.pop(0))

    # check if the queue if empty
    def is_empty (self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size (self):
        return (len(self.queue))

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):

    num_pass = 0 #initial place holder for num passes
    final = []

    for st in a: #finds length of longest string
        if len(st)>num_pass:
            num_pass = len(st)
    
    q_list = [Queue() for i in range(37)] #makes the 0-9,a-z, and lastQ in the list

    q_map = {} #empty dict

    #maps numbers and letters to indicies in q_list
    for i in range(10):
        q_map.update({chr(ord('0') + i):i})
    
    for j in range (26):
        q_map.update({chr(ord('a') + j):j+10})

    #initially puts all strings from a in the last index of q list
    for element in a:
        q_list[len(q_list)-1].enqueue(element)


    #starts at highest length string, and fills and refills the queues in the qlist until num pass goes to 0.
    for i in range (num_pass-1, -1,-1):
        while not q_list[len(q_list)-1].is_empty():
            temp = q_list[len(q_list)-1].dequeue()
            if len(temp)<i+1:
                loc = '0'
            else:
                loc = temp[i]
            q_list[q_map[loc]].enqueue(temp)

        #puts all the elements in other queues back into the last list for the next pass
        for x in range (len(q_list)-1):
            while not q_list[x].is_empty():
                q_list[len(q_list)-1].enqueue(q_list[x].dequeue())

    
    last_Q = q_list[len(q_list)-1] 
    #puts all elements of the last q into the final list
    while not last_Q.is_empty():
        final.append(last_Q.dequeue())

    return final

def main():
    # read the number of words in file
    line = sys.stdin.readline()
    line = line.strip()
    num_words = int (line)

    # create a word list
    word_list = []
    for i in range (num_words):
        line = sys.stdin.readline()
        word = line.strip()
        word_list.append (word)

    '''
    # print word_list
    print (word_list)
    '''

    # use radix sort to sort the word_list
    sorted_list = radix_sort (word_list)

    # print the sorted_list
    print (sorted_list)

if __name__ == "__main__":
    main()