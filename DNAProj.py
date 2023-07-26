#  File: DNA.py

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





def longest_subsequence (s1, s2):

    subsequence_array = []
    str_seq = ""
    
    for i in range(len(s1)):
        for j in range(len(s2)):
            c1 = i
            c2 = j
            while c1 < len(s1) and c2 < len(s2) and s1[c1] == s2[c2]:
                str_seq += s1[c1]
                c1 += 1
                c2 += 1
            if str_seq:
                subsequence_array.append(str_seq) 
            str_seq = ""
    
    # find a way to get all maxes + sort
    return max(subsequence_array)



longest_subsequence("GAAGGTCGAA", "CCTCGGGA")







# def main():

# 	#read the number of pairs

# 	num_pairs = sys.stdin.readline()
# 	num_pairs = num_pairs.strip()
# 	num_pairs = int (num_pairs)
	

# 	print(num_pairs)


# if __name__ == "__main__":
#   main()


