#  File: Reducible.py

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
import math

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
    if (n == 1):
        return False

    limit = int (n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
    hash_idx = 0
    for j in range (len(s)):
        letter = ord (s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size(s, const):
    step = 0
    for let in s: #goes thorugh string and converts to key
        val = ord(let) - 96
        step = const - (step * 26 + val) % const #uses double hashing formula to add to ste size
    return step



#Input: an index idx, and a hash table
#Output: returns true if the hashtable is empty at the specified index.
def is_empty(idx,hash_table):
    if (hash_table[idx]==''): #checks if element is empty string
        return True
    else:
        return False

#input: hash table
#output: boolean true if the hash table is full
def table_full(hash_table):
    return '' not in hash_table 

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
    if table_full(hash_table): #checks to see if the table is full
        print('table full')
        return
    step = step_size(s,11) #finds the step sized used for double hashing for s.
    idx = hash_word(s, len(hash_table)) #starting index to begin search for empty index to place s 
    x = 1
    while(not is_empty(idx, hash_table)): # goes through hash table, incrementing by step size looking for a place to store s.
        idx = (idx+(x*step))%len(hash_table)

    hash_table[idx] = s

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise

def find_word (s, hash_table):
    step = step_size(s,11) #finds the step sized used for double hashing for s.
    idx = hash_word(s, len(hash_table)) #starting index to begin search for s.
    x = 1
    while(hash_table[idx]!=s): #goes through hashtable, until s is found or an empty string is found.
        idx = (idx+(x*step))%len(hash_table)
        if hash_table[idx] == '':
            break

    return hash_table[idx]==s #returns whether or not the idx recieved from the while loop contains s.

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
    largest_words = []
    max_len = 0
    for word in string_list:
        if len(word) > max_len:
            max_len = len(word)
            largest_words = [word]
        elif len(word) == max_len:
            largest_words.append(word)
    largest_words = sorted(largest_words)
    for i in range(len(largest_words)):
        print(largest_words[i])

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
    if s == 'a' or s == 'i' or s == 'o': #base case returns true if s is any of the 3 letters.
        return True
    
    if find_word(s, hash_memo): #base case returns true if s already in memo.
        return True
    
    if not find_word(s, hash_table): #base case returns false if s not in memo.
        return False
    
    if not 'a' in s and not 'o' in s and not 'i' in s: #base case returns false if these 3 letters are not in s.
        return False
    
    for i in range(len(s)): #goes thru s and gets all substrings taking only one letter out at a time.
        ssub = s[:i] + s[i+1:]
        if is_reducible(ssub, hash_table, hash_memo):#adds the string to memo if its not already in memo and it is reducible
            if not find_word(s, hash_memo):
                insert_word(s, hash_memo)
            return True
    
    return False


def main():
    # create an empty word_list
    word_list = []

    # read words from words.txt and append to word_list
    for line in sys.stdin:
        line = line.strip()
        word_list.append(line)

    # find length of word_list
    n = len(word_list)
    N = 2*n

    # determine prime number N that is greater than twice
    # the length of the word_list

    while(not is_prime(N)):
        N+=1


    # create an empty hash_list
    # populate the hash_list with N blank strings

    hash_list = ['' for i in range (N)]

    # hash each word in word_list into hash_list
    # for collisions use double hashing

    for word in word_list:
        insert_word(word, hash_list) 

    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than 
    # 0.2 * size of word_list

    M = N

    while (not is_prime(M)):
        M+=1

    # populate the hash_memo with M blank strings

    hash_memo = ['' for i in range (M)]


    # create an empty list reducible_words

    reducible_words = []

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    # as you recursively remove one letter at a time check
    # first if the sub-word exists in the hash_memo. if it does
    # then the word is reducible and you do not have to test
    # any further. add the word to the hash_memo.

    for word in word_list:
        if is_reducible(word, hash_list, hash_memo):
            reducible_words.append(word)
    # find the largest reducible words in reducible_words
    get_longest_words(reducible_words)
    # print the reducible words in alphabetical order
    # one word per line

if __name__ == "__main__":
    main()