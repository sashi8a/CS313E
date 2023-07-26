#  File: TopoSort.py

#  Description:

#  Student Name: Sashi Ayyalasomayajula

#  Student UT EID: sa55645

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 11/27/22

#  Date Last Modified: 11/28/22


import sys

class Stack (object):
    def __init__ (self):
        self.stack = []

    # add an item to the top of the stack
    def push (self, item):
        self.stack.append (item)

    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek (self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty (self):
        return (len (self.stack) == 0)

    # return the number of elements in the stack
    def size (self):
        return (len (self.stack))


class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty (self):
        return (len (self.queue) == 0)

    # return the size of the queue
    def size (self):
        return (len (self.queue))


class Vertex (object):
    def __init__ (self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited (self):
        return self.visited

  # determine the label of the vertex
    def get_label (self):
        return self.label

  # string representation of the vertex
    def __str__ (self):
        return str (self.label)


class Graph (object):
    def __init__ (self):
        self.Vertices = []
        self.adjMat = []

  # check if a vertex is already in the graph
    def has_vertex (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

  # given the label get the index of a vertex
    def get_index (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

  # add a Vertex with a given label to the graph
    def add_vertex (self, label):
        if (self.has_vertex (label)):
            return

        # add vertex to the list of vertices
        self.Vertices.append (Vertex (label))

        # add a new column in the adjacency matrix
        nVert = len (self.Vertices)
        for i in range (nVert - 1):
            (self.adjMat[i]).append (0)

        # add a new row for the new vertex
        new_row = []
        for i in range (nVert):
            new_row.append (0)
        self.adjMat.append (new_row)

  # add weighted directed edge to graph
    def add_directed_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
    def add_undirected_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i

        return -1

  # do a depth first search in a graph
    def dfs (self, v):
        # create the Stack
        theStack = Stack ()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])
        theStack.push (v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
            print (self.Vertices[u])
            theStack.push (u)

        # the stack is empty, let us rest the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False


    def delete_edge (self, fromVertexLabel, toVertexLabel):

        from_idx = self.get_index(fromVertexLabel)
        to_idx = self.get_index(toVertexLabel)
        test3 = self.adjMat.copy()
        #could have done self.adjMat or test3. same difference.


        if from_idx!=-1 and to_idx!=-1: #checks if vertex exists

            if test3[from_idx][to_idx] == test3[to_idx][from_idx]:
                test3[from_idx][to_idx] = 0
                test3[to_idx][from_idx] = 0
            else:
                test3[from_idx][to_idx] = 0

        return test3

    def delete_vertex (self, vertexLabel):

        idx = self.get_index(vertexLabel)
        duplicate = self.get_vertices()
        duplicate.remove(duplicate[idx])


        for vertex in duplicate:
            print(vertex)


        length = len(self.adjMat)

        for i in range(length):
            value = self.adjMat[i][idx]
            self.adjMat[i].pop(idx) #pops the column out for specified vertex

        self.adjMat.remove(self.adjMat[idx]) #pops the row out for specified vertex


  # do the breadth first search in a graph
    def bfs (self, v):
        #0. creating Queue
        frontierqueue = Queue()

        #currentv = self.Vertices[v]
        currentv = v
        frontierqueue.enqueue(v)
        discoveredset = []
        (self.Vertices[v]).visited = True

        #2. Visit an adjacent unvisited vertex (if there is one) in
        #order from the current vertex. Mark it visited and insert
        #it into the queue.
        while (not frontierqueue.is_empty()):

            currentv = frontierqueue.dequeue()
            self.Vertices[currentv].visited = True

            idx = self.Vertices[currentv].get_label()

            lst = self.get_neighbors(idx)
            print(idx) #PRINTS the bfs traversal


            discoveredset.append(currentv)

            for adjVertex in lst:


                if adjVertex not in discoveredset:
                    discoveredset.append(adjVertex)
                    frontierqueue.enqueue(adjVertex)


        # the Queue is empty, let us reset the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False

        return


  # determine if a directed graph has a cycle
  # this function should return a boolean and not print the result
    def has_cycle (self):
        return

  # return a list of vertices after a topological sort
  # this function should not print the list
    def toposort (self):
        return

def main():
    # create the Graph object
    cities = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int (line)

    # read the vertices to the list of Vertices
    for i in range (num_vertices):
        line = sys.stdin.readline()
        city = line.strip()
        cities.add_vertex (city)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int (line)

    # read each edge and place it in the adjacency matrix
    for i in range (num_edges):
        line = sys.stdin.readline()
        edge = line.strip()
        edge = edge.split()
        start = int (edge[0])
        finish = int (edge[1])
        weight = int (edge[2])

        cities.add_directed_edge (start, finish, weight)

    # read the starting vertex for dfs and bfs
    line = sys.stdin.readline()
    start_vertex = line.strip()

    # get the index of the starting vertex
    start_index = cities.get_index (start_vertex)

    # do the depth first search
    print ("Depth First Search")
    cities.dfs (start_index)
    print ()
    
if __name__ == "__main__":
    main()