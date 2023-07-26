#  File: ExpressionTree.py

#  Description: 

#  Student Name: Sashi Ayyalasomayajula

#  Student UT EID: sa55465

#  Partner Name: Monica Pham

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def length(self):
        return len(self.stack)

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        self.root = Node()
        current = self.root
        expr_stack = Stack()
        tokens_list = expr.split(' ')
        for i in range(len(tokens_list)):
            item = tokens_list[i]
            if item == '(':
                current.lChild = Node()
                expr_stack.push(current)
                current = current.lChild
            elif item in operators:
                current.data = item
                expr_stack.push(current)
                current.rChild = Node()
                current = current.rChild
            elif item == ')':
                if not expr_stack.is_empty():
                    current = expr_stack.pop()
            else:
                if '.' in item:
                    current.data = float(item)
                    if not expr_stack.is_empty():
                        current = expr_stack.pop()
                else:
                    current.data = int(item)
                    if not expr_stack.is_empty():
                        current = expr_stack.pop()



    
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        if aNode.data in operators:
            if aNode.data == '+':
                return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
            if aNode.data == '-':
                return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild)
            if aNode.data == '*':
                return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
            if aNode.data == "/":
                return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
            if aNode.data == "//":
                return self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild)
            if aNode.data == "%":
                return self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild)
            if aNode.data == "**":
                return self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild)
        else:
            return float(aNode.data) 
        
    #uses an extra parameter arr to store the contents of the string through recursive calls
    def pre_order_helper(self, aNode, arr):
        current = aNode
        if  current!=None:

            arr.append(str(current.data)) #C
            if current.lChild!=None:
                self.pre_order_helper(current.lChild,arr) #L

            if current.rChild!=None:
                self.pre_order_helper(current.rChild,arr) #R

    
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode): #CLR
        arr = []
        self.pre_order_helper(aNode,arr)
        s = ''
        for let in arr:
            s+=let+' ' #appends all elements of arr into string format
        return s

    #uses an extra parameter arr to store the contents of the string through recursive calls
    def post_order_helper(self,aNode,arr):
        current = aNode
        if current!=None:

            if current.lChild!=None:
                self.post_order_helper(current.lChild,arr) #L

            if current.lChild!=None:
                self.post_order_helper(current.rChild,arr) #R

            arr.append(str(current.data)) #C

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode): #LRC
        arr = []
        self.post_order_helper(aNode,arr)
        s = ''
        for let in arr:     #appends all elements of arr into string format
            s+=let+' '

        return s




# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", (tree.pre_order(tree.root)).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", (tree.post_order(tree.root)).strip())

if __name__ == "__main__":
    main()