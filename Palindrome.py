#  File: Palindrome.py

#  Description:

#  Student Name: Sashi Ayyalaosomayajula

#  Student UT EID: sa55465

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:


import sys

# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be 
#         made by adding characters to the start of the input string
def smallest_palindrome(str):

    begaddon = '' #empty string to append to the beginning of str
    pal = '' #empty string for final palindrome
    while (not is_pal(str)): #while str is not a palindrome, add the last character to begaddon, and check if str without the last character is a palindrome

        begaddon+= str[-1]
        str = str[0:-1]

    endaddon = begaddon[::-1] #end addon will be appended to the end of str once the while loop breaks
    pal = begaddon+str+endaddon #pal is the combination of begaddon, str and endaddon
        
    return pal
    


# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a boolean that is True if the given string is a palindrome
def is_pal(str):

    rev_str = str[::-1] #checks if reverse of str is equal to str
    return str == rev_str


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  assert smallest_palindrome('aaaadnh') == 'hndaaaadnh'
  assert smallest_palindrome('') == ''

  return "all test cases passed"

def main():
    # run your test cases
    

    #print (test_cases())
    

    # read the data

    f = sys.stdin.readlines()

    counter = 0

    #prints out results
    while(counter<=len(f)-1):

        curr_str = str(f[counter].strip())
        print(smallest_palindrome(curr_str))
        counter+=1

if __name__ == "__main__":
  main()