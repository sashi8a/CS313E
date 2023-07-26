def sub_sets (a,b,idx):
    hi = len(a)
    if (idx == hi):
        print(b)
        return
    else:
        c = b[:]
        b.append(a[idx])
        sub_sets(a,b,idx+1)
        sub_sets(a,c,idx+1)


def main():
    a = ['A','B','C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    b = []
    sub_sets(a,b,0)


main()
