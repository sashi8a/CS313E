import math
import sys





def main():

    num_rings = int(input())
    x = list(map(int, input().split()))

    # print n-1 lines
    # each line contains A/B in reduced form
    # format: "1/2"

    
    num_teeth_first = x[0]

    rotations = []

    for i in range (1,num_rings):
        
        GCF = find_GCD(num_teeth_first,x[i])

        if (num_teeth_first==x[i]):
            rotations.append('1/1')
        elif (num_teeth_first>x[i]) and (num_teeth_first%x[i]==0):
            rotations.append(str(num_teeth_first//x[i])+'/1')
        elif (num_teeth_first>x[i]) and (num_teeth_first%x[i]!=0):
            rotations.append(str(num_teeth_first//GCF)+'/'+str(x[i]//GCF))
        elif (num_teeth_first<x[i]):
            rotations.append(str(num_teeth_first//GCF)+'/'+str(x[i]//GCF))


    for rot in rotations:
        print(rot)
        


def find_GCD(a,b):

    if (b==0):
        return a
    else:
        return find_GCD(b, a%b)



if __name__ == "__main__":
    main()
