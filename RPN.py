

class Stack (object):
  def __init__ (self):
      self.stack = []

  # add an item to the top of the stack
  def push_on (self, item):
      self.stack.append ( item )

  def push_at (self,item,n):
      self.stack[n] = item

  # remove an item from the top of the stack
  def pop (self,n):
      return self.stack.pop(n)

  # check what item is on top of the stack without removing it
  def peek (self,n):
      return self.stack[n]

  # check if a stack is empty
  def isEmpty (self):
      return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
      return (len(self.stack))

  def __str__(self):
      s = ''
      for c in self.stack:
          s+=c
      return s




def compute_RPN(s):
    ops = ['%','*','+','-','//','/','**']
    RPN = Stack()
    for c in s:
        RPN.push_on(c)

    counter = 0
    while counter<RPN.size():
        print(str(RPN))
        print('I-->',counter)
        x = RPN.peek(counter)
        if x in ops:
            a = RPN.peek(counter)
            b = RPN.peek(counter-1)
            c = RPN.peek(counter-2)
            temp = compute(a,b,c)
            RPN.push_at(temp,counter)

            RPN.pop(counter-1)
            RPN.pop(counter-2)
            counter-=2
        else:
            counter+=1

    return RPN.peek(0)


            



def compute(a,b,c):
    return str(eval(c+a+b))




def main():
    print(compute_RPN('74+3-25*/'))

main()