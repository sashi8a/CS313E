#  File: Poly.py

#  Description:

#  Student Name: Sashi Ayyalasomayajula

#  Student UT EID: sa55465

#  Partner Name: Alexander Pinnarwan

#  Partner UT EID: acp3576

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:


import sys

class Link (object):
    def __init__ (self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__ (self):
        return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
    def __init__ (self):
        self.first = None

    def setfirst(self):
        self.first = Link(3,5)
        self.insert_in_order(2,6)


    #returns true if a term with a similar exponent already exists within the polynomial
    def exp_in_list(self,exp):
        current = self.first

        yes = False

        while current!=None:
            if current.exp==exp:
                yes = True

            current = current.next

        return yes

  # keep Links in descending order of exponents
    def insert_in_order (self, coeff, exp):
        current = self.first
        newLink = Link(coeff,exp)
        if current==None: #if empty, new link is first
            self.first = newLink
        elif current.next==None: #if only one element in list, see if exp of newlink is greater or equal or less, then set accordingly
            if current.exp<newLink.exp:
                self.first = newLink
                newLink.next = current
            elif current.exp==newLink.exp:
                current.coeff+=int(newLink.coeff)
            else:
                current.next = newLink
        else: #if more than 2 elements in list, go through until you find an exponent less than or equal to newlink.exp and set accordingly
            previous = self.first
            inserted = False
            
            if self.exp_in_list(exp): #method used to see if there already exists an element with the same exp. If true, find element and add coefficients
                while current!=None:
                    if current.exp==newLink.exp:
                        current.coeff+=int(newLink.coeff)
                        break

                    current = current.next
            else:  
                while(current!=None):
                    if current.exp<newLink.exp:

                        if current!=self.first:
                            previous.next = newLink
                            newLink.next = current
                        else:
                            self.first = newLink
                            newLink.next = current
                        inserted = True
                        break
                    elif current.exp==newLink.exp: #adding coefficients for same exp
                        current.coeff+=int(newLink.coeff)
                        break

                    previous = current
                    current = current.next

                if not inserted: #if no element has an exponent less than newlinks, and newlinks exp is already not in the list, add newlink at the end
                    previous.next = newLink

                

  # get number of links 
    def get_num_links(self):
        num = 0
        curr = self.first

        while (curr != None):
            if curr.coeff!=0:
                num += 1
            curr = curr.next

        return num

  # add polynomial p to this polynomial and return the sum
    def add (self, p):
        sum_poly = LinkedList()

        selfcurr = self.first
        pcurr = p.first

        while (selfcurr!=None) and (pcurr!=None): #while both lists are currently on a non -None element

            if selfcurr.exp==pcurr.exp: #if the exps are equal, add coefficients

                if selfcurr.coeff+pcurr.coeff!=0: #if the coefficients cancell, move on to next element
                    sum_poly.insert_in_order(int(selfcurr.coeff)+int(pcurr.coeff),selfcurr.exp)
                    selfcurr = selfcurr.next
                    pcurr = pcurr.next
                    continue
                else:
                    selfcurr = selfcurr.next
                    pcurr = pcurr.next
                    continue
            elif selfcurr.exp>pcurr.exp: #if self exp is greater, add to list and only move self to next list and keep pcurr
                sum_poly.insert_in_order(selfcurr.coeff,selfcurr.exp)
                selfcurr = selfcurr.next
                continue
            elif pcurr.exp>selfcurr.exp: #viceversa if pcurr exp is greater
                sum_poly.insert_in_order(pcurr.coeff,pcurr.exp)
                pcurr = pcurr.next
                continue



        if (selfcurr==None) and (pcurr!=None): #if one of the lists have reached the end, append the rest of the other list to the sum list.
            while pcurr!=None:
                sum_poly.insert_in_order(pcurr.coeff,pcurr.exp)
                pcurr = pcurr.next

        if (pcurr==None) and (selfcurr!=None):
            while selfcurr!=None:
                sum_poly.insert_in_order(selfcurr.coeff,selfcurr.exp)
                selfcurr = selfcurr.next
 
        return sum_poly
    


        

  # multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        mult_L = LinkedList()
        pcurr = p.first
        self_first = self.first
        selfcurr = self.first
        while pcurr!=None: #go through all elements of pcurr
            selfcurr = self_first
            while selfcurr!=None: #for each element in pcurr, multiply and append the result for each element in self
                mult_L.insert_in_order(pcurr.coeff*selfcurr.coeff,pcurr.exp+selfcurr.exp)
                selfcurr = selfcurr.next #move on to next element in self
            pcurr = pcurr.next #move on to next element in p
        return mult_L



  # create a string representation of the polynomial
    def __str__ (self):
        s = ''
        current = self.first
        if current==None: #if list is empty print ''
            return s
        else:
            while current!=None:

                if current.coeff==0: #dont print the element if the coefficient is zero
                    current = current.next
                    continue
                if (current.next!=None): #if not last element, add the +
                    s+='('+str(current.coeff)+', '+str(current.exp)+') + '
                else:
                    s+='('+str(current.coeff)+', '+str(current.exp)+')'
                current = current.next


        return s

            


def main():
  # read data from file poly.in from stdin

  f = sys.stdin.readlines()
  #f = open('/Users/sashi_ayyalasomayajula/Downloads/CS313E Programs/poly.in','r').readlines()

  N_1 = int(f[0].strip())

  N_2 = int(f[N_1+2])

  index_of_q = N_1+3

  P = LinkedList()
  Q = LinkedList()

  # create polynomial p

  for i in range (1,N_1+1):
        line = f[i].strip().split(' ')
        coeffP,expP = int(line[0]),int(line[1])
        P.insert_in_order(coeffP,expP)


  # create polynomial q

  for j in range (index_of_q,index_of_q+N_2):
        line = f[j].strip().split()
        coeffQ,expQ = int(line[0]),int(line[1])
        Q.insert_in_order(coeffQ,expQ)

  # get sum of p and q and print sum
  #print('P',P)

  #print('Q',Q)


  print(P.add(Q))

  # get product of p and q and print product
  print(P.mult(Q))

if __name__ == "__main__":
  main()