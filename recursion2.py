#  File: recursion2.py 

#  Description:

#  Student Name: Sashi Ayyalasomayajula

#  Student UT EID: sa55465

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:


# Given an array of ints, is it possible to choose a group of some 
# of the ints, such that the group sums to the given target? 
# This is a classic backtracking recursion problem. Once you 
# understand the recursive backtracking strategy in this problem, 
# you can use the same pattern for many problems to search a space 
# of choices. Rather than looking at the whole array, our convention 
# is to consider the part of the array starting at index start and 
# continuing to the end of the array. The caller can specify the 
# whole array simply by passing start as 0. No loops are needed -- 
# the recursive calls progress down the array. 
def groupSum(start, nums, target):

    
    
    if start<len(nums):

        element = nums[start]

    if(start > len(nums)-1):

        return target == 0 #returns true if the sum of values in nums is equal to target, false if not
    else:

        if(groupSum(start + 1, nums, target - element)): #if start is within nums, returns true if recursive call to groupSum with current element added to sum.
            return True

        if(groupSum(start + 1, nums, target)): #if start is within nums, calls groupsum againat next index without adding current element to sum.
            return True

        return False 
    


  
# Given an array of ints, is it possible to choose a group of some 
# of the ints, beginning at the start index, such that the group 
# sums to the given target? However, with the additional constraint 
# that all 6's must be chosen. (No loops needed.)
def groupSum6(start, nums, target):

    if start<len(nums):

        element = nums[start]

    if(start > len(nums)-1): 
        return target == 0 #returns true if the sum of values in nums is equal to target, false if not

    else: #if start is an index within nums

        if(element==6):
            return groupSum6(start+1, nums, target-element) #if the current element in nums is 6, returns group in next index of list with target-6.

        if (groupSum6(start+1, nums, target-element)): #if start is an index in nums but nums[start]!=6, return true if groupsum6 at the next index with target-element is true.
            return True
    
        return groupSum6(start+1, nums, target) #return groupsum6 starting at the next index with no difference in the value of target.



  
# Given an array of ints, is it possible to choose a group of some 
# of the ints, such that the group sums to the given target with this 
# additional constraint: If a value in the array is chosen to be in 
# the group, the value immediately following it in the array must 
# not be chosen. (No loops needed.) 
def groupNoAdj(start, nums, target):

    if start<len(nums):

        element = nums[start]

    if(start > len(nums)-1): 
        return target == 0 #returns true if the sum of values in nums is equal to target, false if not

    else: #if start is an index within nums

        if (groupNoAdj(start+2, nums, target-element)): #if start is an index in nums return true if groupNoAdj at 2 indicies after with target-element is true.
            return True
    
        return groupNoAdj(start+1, nums, target) #return groupNoAdj starting at the next index with no difference in the value of target.



# Given an array of ints, is it possible to choose a group 
# of some of the ints, such that the group sums to the given 
# target with these additional constraints: all multiples of 
# 5 in the array must be included in the group. If the value 
# immediately following a multiple of 5 is 1, it must not 
# be chosen. (No loops needed.)
def groupSum5(start, nums, target):

    if start<len(nums):

        element = nums[start]

    if(start > len(nums)-1): 
        return target == 0 #returns true if the sum of values in nums is equal to target, false if not

    else: #if start is an index within nums

        if(element%5==0):

            if(start<len(nums)-1):

                if(nums[start+1]==1):
                    return groupSum5(start+2, nums, target-element) #if the current element in nums is a multiple of 5 and the element after is 1, returns groupsum5 2 indicies after with target-element
                else:
                    return groupSum5(start+1, nums, target-element) #if the current element in nums is a multiple of 5 and the element after is not 1, returns groupsum5 at the next index with target-element

            
        if (groupSum5(start+1, nums, target-element)): #if start is an index return true if groupsum5 at the next index with target-element is true.
            return True
    
        return groupSum5(start+1, nums, target) #return groupsum5 starting at the next index with no difference in the value of target.
  
  
  
# Given an array of ints, is it possible to choose a 
# group of some of the ints, such that the group sums 
# to the given target, with this additional constraint: 
# if there are numbers in the array that are adjacent 
# and the identical value, they must either all be chosen, 
# or none of them chosen. For example, with the array 
# [1, 2, 2, 2, 5, 2], either all three 2's in the middle 
# must be chosen or not, all as a group. (one loop can 
# be used to find the extent of the identical values). 
def groupSumClump(start, nums, target):

    if start<len(nums):

        element = nums[start]

    if(start > len(nums)-1): #same base case as previous
        return target == 0 #returns true if the sum of values in nums is equal to target, false if not

    else:
        next_ind = start + 1 #stores index value directly after start
        while(next_ind < len(nums) and nums[start] == nums[next_ind]): #checks is next element is same as num[start] and if next index is within nums
            next_ind += 1 #increments next index

        num_same_element = next_ind-start #caluculates the number of similar elements
        if(groupSumClump(next_ind, nums, target - (num_same_element * element))): #recursive call which adds all instances of the similar element to the target sum, returns True if equals target
            return True

        return(groupSumClump(next_ind, nums, target)) # recursive call which doesn't add all similar elements to target sum, and continues through nums.


  
  

# Given an array of ints, is it possible to divide the 
# ints into two groups, so that the sums of the two 
# groups are the same. Every int must be in one group 
# or the other. Write a recursive helper method that 
# takes whatever arguments you like, and make the 
# initial call to your recursive helper from splitArray(). 
# (No loops needed.)
def splitArray(nums):
    return splitArrayHelper(0,nums,0)


def splitArrayHelper(start, nums, target):

    if start<len(nums):

        element = nums[start]

    if start>(len(nums)-1): #similar base case as previous
        return target==0

    else:
        if(splitArrayHelper(start+1, nums, target+element)): #recursive call to helper which adds current element to target
            return True
        
        return splitArrayHelper(start+1, nums, target-element) #recursive call to helper which subtracts element from target

    #in the end the funciton will output true if base case returns true, so if target is added up to some value N and then subtracted back
    # to zero, it would mean that 2 groups of ints have the same sum so that N +(-N) = 0

	
	
# Given an array of ints, is it possible to divide the 
# ints into two groups, so that the sum of one group
# is a multiple of 10, and the sum of the other group 
# is odd. Every int must be in one group or the other. 
# Write a recursive helper method that takes whatever 
# arguments you like, and make the initial call to your 
# recursive helper from splitOdd10(). (No loops needed.)
def splitOdd10(nums):
    return splitOdd10Helper(0,0,0,nums)

  
def splitOdd10Helper(group1_sum,group2_sum, start, nums):

    if start<len(nums):

        element = nums[start]

    if start>(len(nums)-1):
        return ((group1_sum%10==0 and group2_sum%2==1) or (group1_sum%2==1 and group2_sum%10==0)) #returns whether or not given constraint is true.

    else:
        return splitOdd10Helper(group1_sum+element, group2_sum, start+1, nums) or splitOdd10Helper(group1_sum, group2_sum+element, start+1, nums) # returns either helper with element added to group1 or group2 sum depending on which is True


  
# Given an array of ints, is it possible to divide the ints 
# into two groups, so that the sum of the two groups is the 
# same, with these constraints: all the values that are 
# multiple of 5 must be in one group, and all the values 
# that are a multiple of 3 (and not a multiple of 5) 
# must be in the other. (No loops needed.) 
def split53(nums):
    return split53Helper(0,nums,0)

def split53Helper(start, nums, target):

    if start<len(nums):

        element = nums[start]

    if start>(len(nums)-1): #similar base case as previous
        return target==0
    else:
        if(element%5==0): #if element is multiple of 5, recursive call to helper with element added to target sum 
            return split53Helper(start+1, nums, target+element)
        
        if(element%3==0): #if element is multiple of 3, recursive call to helper with element subtracted to target sum 
            return split53Helper(start+1, nums, target-element)

        # adding when multiple of 5 and subtracting when multiple of 3 creates 2 groups that act on the target sum based on the multiple of the element

        if(split53Helper(start+1, nums, target+element)): #returns True if target = 0 in the end, indicating that 5 and 3 groups have the same sum.
            return True
        
        return split53Helper(start+1, nums, target-element) #if start has not exceeded nums, will return true or false depending on the final value of target. (base case)



    





#######################################################################################################
#######################################################################################################
#                                                                                                     #
#                   DO NOT MODIFY ANYTHING BELOW THIS LINE !!                                         #
#                                                                                                     #
#######################################################################################################
#######################################################################################################
def main(argv):
    problems = ["groupSum", "groupSum6", "groupNoAdj", "groupSum5", "groupSumClump", "splitArray", "splitOdd10", "split53"]
    if len(argv) == 0:
        printHelp()
        exit(1)
    elif "all" in argv:
        argv = problems
    for problem in argv:
        if not problem in problems:
            printHelp()
            exit(1)
    
    groupSum_args = [(0, [2, 4, 8], 10), (0, [2, 4, 8], 14), (0, [2, 4, 8], 9), (0, [2, 4, 8], 8), (1, [2, 4, 8], 8), (1, [2, 4, 8], 2), (0, [1], 1), (0, [9], 1), (1, [9], 0), (0, [], 0), (0, [10, 2, 2, 5], 17), (0, [10, 2, 2, 5], 15), (0, [10, 2, 2, 5], 9)]
    groupSum6_args = [(0, [5, 6, 2], 8), (0, [5, 6, 2], 9), (0, [5, 6, 2], 7), (0, [1], 1), (0, [9], 1), (0, [], 0), (0, [3, 2, 4, 6], 8), (0, [6, 2, 4, 3], 8), (0, [5, 2, 4, 6], 9), (0, [6, 2, 4, 5], 9), (0, [3, 2, 4, 6], 3), (0, [1, 6, 2, 6, 4], 12), (0, [1, 6, 2, 6, 4], 13), (0, [1, 6, 2, 6, 4], 4), (0, [1, 6, 2, 6, 4], 9), (0, [1, 6, 2, 6, 5], 14), (0, [1, 6, 2, 6, 5], 15), (0, [1, 6, 2, 6, 5], 16)]
    groupNoAdj_args = [(0, [2, 5, 10, 4], 12), (0, [2, 5, 10, 4], 14), (0, [2, 5, 10, 4], 7), (0, [2, 5, 10, 4, 2], 7), (0, [2, 5, 10, 4], 9), (0, [10, 2, 2, 3, 3], 15), (0, [10, 2, 2, 3, 3], 7), (0, [], 0), (0, [1], 1), (0, [9], 1), (0, [9], 0), (0, [5, 10, 4, 1], 11)]
    groupSum5_args = [(0, [2, 5, 10, 4], 19), (0, [2, 5, 10, 4], 17), (0, [2, 5, 10, 4], 12), (0, [2, 5, 4, 10], 12), (0, [3, 5, 1], 4), (0, [3, 5, 1], 5), (0, [1, 3, 5], 5), (0, [3, 5, 1], 9), (0, [2, 5, 10, 4], 7), (0, [2, 5, 10, 4], 15), (0, [2, 5, 10, 4], 11), (0, [1], 1), (0, [9], 1), (0, [9], 0), (0, [], 0)]
    groupSumClump_args = [(0, [2, 4, 8], 10), (0, [1, 2, 4, 8, 1], 14), (0, [2, 4, 4, 8], 14), (0, [8, 2, 2, 1], 9), (0, [8, 2, 2, 1], 11), (0, [1], 1), (0, [9], 1)]
    splitArray_args = [([2, 2]), ([2, 3]), ([5, 2, 3]), ([5, 2, 2]), ([1, 1, 1, 1, 1, 1]), ([1, 1, 1, 1, 1]), ([]), ([1]), ([3, 5]), ([5, 3, 2]), ([2,2,10,10,1,1]), ([1,2,2,10,10,1,1]), ([1,2,3,10,10,1,1])]
    splitOdd10_args = [[5, 5, 5], [5, 5, 6], [5, 5, 6, 1], [6, 5, 5, 1], [6, 5, 5, 1, 10], [6, 5, 5, 5, 1], [1], [], [10, 7, 5, 5], [10, 0, 5, 5], [10, 7, 5, 5, 2], [10, 7, 5, 5, 1]]
    split53_args = [[1,1], [1, 1, 1], [2, 4, 2], [2, 2, 2, 1], [3, 3, 5, 1], [3, 5, 8], [2, 4, 6], [3, 5, 6, 10, 3, 3]]
	
	
    groupSum_ans = [True, True, False, True, True, False, True, False, True, True, True, True, True]
    groupSum6_ans = [True, False, False, True, False, True, True, True, False, False, False, True, True, False, False, True, True, False]
    groupNoAdj_ans = [True, False, False, True, True, True, False, True, True, False, True, True]
    groupSum5_ans = [True, True, False, False, False, True, True, False, False, True, False, True, False, True, True]
    groupSumClump_ans = [True, True, False, True, False, True, False]
    splitArray_ans = [True, False, True, False, True, False, True, False, False, True, True, False, True]
    splitOdd10_ans = [True, False, True, True, True, False, True, False, True, False, True, False]
    split53_ans = [True, False, True, False, True, False, True, True]

    for prob in argv:
      correct = 0  # counts number of test cases passed
      leftParen = "("
      rightParen = ")"
      # loop over test cases
      for i in range(len(locals()[prob+"_args"])):
        if type(locals()[prob+"_args"][i]) is tuple:
          leftParen = rightParen = ""
        if (type(locals()[prob+"_args"][i]) is str) or (type(locals()[prob+"_args"][i]) is int) or (type(locals()[prob+"_args"][i]) is list) or (len(locals()[prob+"_args"][i]) == 1): # function takes one argument
          if globals()[prob](locals()[prob+"_args"][i]) == locals()[prob+"_ans"][i]:
              print ("\nCorrect!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](locals()[prob+"_args"][i])), " expected:", str(locals()[prob+"_ans"][i]))
              correct += 1
          else: # print fail message
              print ("\nWrong!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](locals()[prob+"_args"][i])), " expected:", str(locals()[prob+"_ans"][i]))
        elif len(locals()[prob+"_args"][i]) == 2: # there are two arguments to function
          first, second = locals()[prob+"_args"][i]
          if globals()[prob](first, second) == locals()[prob+"_ans"][i]:
              print ("\nCorrect!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](first, second)), " expected:", str(locals()[prob+"_ans"][i]))
              correct += 1
          else: # print fail message
              print ("\nWorng!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](first, second)), " expected:", str(locals()[prob+"_ans"][i]))
        else:    
          first, second, third = locals()[prob+"_args"][i]
          if globals()[prob](first, second, third) == locals()[prob+"_ans"][i]:
              print ("\nCorrect!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](first, second, third)), " expected:", str(locals()[prob+"_ans"][i]))
              correct += 1
          else: # print fail message
              print ("\nWrong!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](first, second, third)), " expected:", str(locals()[prob+"_ans"][i]))
      print ("\n" + prob + ": passed", correct, "out of", len(locals()[prob+"_ans"]), "\n")

def printHelp():
    print ("\nInvoke this script with the name of the function you wish to test.")
    print ("e.g. python recursion1.py factorial")
    print ("Invoke with \"python recursion1.py all\" to run all of the function tests\n")
      
import sys
main(sys.argv[1:])