def find_GCD(a,b):

    if (b==0):
        return a
    else:
        return find_GCD(b, a%b)

print(find_GCD(6389,65546546))