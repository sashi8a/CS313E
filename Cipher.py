#  File: Cipher.py

#  Description: Program made to encrypt and decrypt 2 separate strings using a specific algorithm.

#  Student Name: Sashi Ayyalasomayajula

#  Student UT EID: sa55465

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 9/9/22

#  Date Last Modified: 9/12/22
import sys
import math

# Input: strng is a string of 100 or less of upper case, lower case, and digits
# Output: function returns an encrypted string 

def encrypt (P):

    length_P = len(P) #stores value of the length of P

    M = int(nearest_sqr(length_P)) #calls method to find the nearest greatest square number

    K = int(M**(0.5)) #sets value of squareroot of M

    padded_P = '' #declares empty string to store alters value of P

    #loop that adds a '*' to P until the length has reached a square number
    while len(padded_P)!=M:
        if len(padded_P)<length_P:
            padded_P = P
        else:
            padded_P +='*'

    padded_list = [] #creates empty list to store characters of padded_P

    padded_P_itr = 0 #iterator variable to run through index of padded_P

    #adds every character in padded_P to padded_list
    for i in range(K):

        col = []

        for j in range (K):

            col.append(padded_P[padded_P_itr])
            padded_P_itr+=1
        
        padded_list.append(col)


    #creates a new list that is padded_list rotated 90 degrees clockwise
    shifted_list = rotate_ninety(padded_list)

    encrypted_P = '' #sets empty string to store the encrypted string

    #adds all elements of shifted list to encrypted_P
    for c in range(len(shifted_list)):
        for d in range(len(shifted_list)):

            if shifted_list[c][d]!='*':
                encrypted_P+=shifted_list[c][d]


    return encrypted_P



# Input: strng is a string of 100 or less of upper case, lower case, and digits
# Output: function returns an encrypted string 

def decrypt(Q):
  M = int(nearest_sqr(len(Q))) #nearest square to message length
  K = int(M**0.5) #dimension of table

  #adds asterisks to Q until the length of Q is a perfect square
  while len(Q)!=M:
    Q+='*'

  Y = 0 #iterator variable that goes through Q

  table = []   #creates a new empty 2D list

  #loops through Q and adds every character to table
  for i in range(K):
    row = []
    for j in range(K):
      row.append(Q[Y])
      Y+=1
    table.append(row)
 
  #rotates table 270 degrees clockwise (90 degrees counter clockwise)
  for x in range(3):
    table = rotate_ninety(table)
   
  decrypted = '' #string to store final message
 
  #goes through table and extracts string
  for row in range(K):
    for col in range(K):
      if table[row][col] != '*':
        decrypted += table[row][col]

  return decrypted


# Description: method used to find value of nearest sqare root
# Input: takes in an integer value
# Output: returns an integer value which is the nearest sqaure 
# number greater than or equal to the input integer

def nearest_sqr(L):

    found = False #sets exit case for while loop to false

    while not found:

        if (L**(0.5)).is_integer(): #exits while loop if nearest greatest sqare number is found
            found = True
        else:
            L+=1 #increments L 

    if found:
        return L


#method which augments a 2-d list by rotating it clockwise by ninety degrees
# Input: takes in a 2-d list
# Output: returns a 2-d list that has been shifted clockwise by 90 degrees

def rotate_ninety(list):

    rot_list = [] #creates empty list

    for i in range(len(list)):

        col = [] #creates temp empty column

        for j in range(len(list)-1,-1,-1): #loops through the elements of each column from bottom to top

            col.append(list[j][i]) #adds the element to temp col list
        
        rot_list.append(col)

    return rot_list

def main():


    #reads input file
    f = sys.stdin.readlines()
    P = f[0].strip()
    Q = f[1]

    print(encrypt(P))

    print(decrypt(Q))
main()