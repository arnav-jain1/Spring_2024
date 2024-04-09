# Most of the code below is reused from previous labs, the only change is holding the verts in the graph as a list instead of a dict
class Graph:
    # Graph holds verts and edges as dicts for easy and quick access. 
    def __init__(self) -> None:
        # For vert, the key will be the letter and the value will be the node object
        self.v = []
        # For edges, the key will be the vert and the value will be a set of its edges
        self.adj = dict()

class Node:
    def __init__(self, value) -> None:
        # Has a value, parent (default is self), and rank (default is 0) vars 
        self.value = value
        self.p = self
        self.rank = 0
    # Str method for printing
    def __str__(self) -> str:
        return str(self.value)

# Make tree method which just turns the input into a Node
def make_tree(elem):
    return Node(elem) 

# Find set method with takes in a node
def find_set(node):
    # If the node is not the same as its parent (it is not the root)
    if node != node.p:
        # Set the parent to the root (path compression) by recursively calling the same method upwards
        node.p = find_set(node.p)
    # return the parent which will eventually be the root node so that it can be assigned in the above recursion part
    return node.p

# Union which takes two nodes
def union(node1, node2):
    # Find the root of both nodes
    node1 = find_set(node1)
    node2 = find_set(node2)
    # If the rank of the first node is more than the second, set the parent of the second node to the first node
    if node1.rank > node2.rank:
        node2.p = node1
    # Vice versa
    elif node2.rank > node1.rank:
        node1.p = node2
    # If the ranks are the same
    else:
        # set the parent of the first node to be the second node then increment the rank of the second node
        node1.p = node2
        node2.rank += 1

# Minheap class that was changed a little bit
class MinHeap:
    def __init__(self):
        # Create an array as well as a set full of all the letters that will be stored
        self.heap = []
        self.current_elements = set()

    # Heapify func that takes an array, length of the list, and index (default val is 0)
    def heapify(self, i):
        # L and R indices from slides (adjusted for 0 indexing so it adds 1 and 2 instead of 0 and 1 respectively)
        l = 2 * i + 1
        r = 2 * i + 2

        # Smallest var that is set to i as default
        smallest = i

        size = len(self.heap)

        # If it is in range and left node is less than right node set smallest to left
        if l < size and self.heap[l][1] < self.heap[smallest][1]:
            smallest = l
        # Same but with right
        if r < size and self.heap[r][1] < self.heap[smallest][1]:
            smallest = r

        # If smallest is not i, swap and recurse
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    # Min function to extract the root
    def min(self):
        # Remove the root from the set of elements
        self.current_elements.remove(self.heap[0][0])
        # If the length is 1, just pop and return
        if len(self.heap) == 1:
            return self.heap.pop()
        # Otherwise get the min and pop it
        min = self.heap.pop(0)

        # Then heapify the root
        self.heapify(0)
        return min
    
    # Add function that takes a vert and a key and inserts it into the heap
    def add(self, vert, key):
        # Add to the root and current elements set. then heapify the root
        self.heap.insert(0, (vert, key))
        self.current_elements.add(vert)
        self.heapify(0)
    
    # Decrease key function that takes a vert and a key
    def decrease_key(self, vert, key):
        # Go through the heap and find the vert and pop it
        for i in range(len(self.heap)):
            if self.heap[i][0] == vert:
                self.heap.pop(i)
                break
        # Readd the vert with the new key (not the most efficient but it works for this case)
        self.add(vert, key)




# Where new code begins





# Krusal's algorithm that takes in verts and edges
def kruskal(verts, edges):
    # A is the set that will hold the edges of the MST
    A = set()
    # Nodes dict that will hold the verts as keys and the nodes as values
    nodes = dict()
    # Go through the verts and make a tree for each
    for vert in verts:
        nodes[vert] = make_tree(vert)

    # Go through the edges 
    for edge in edges:
        # Set u,v to the letters and w to the weight
        u, v, w = edge
        # If they aren't in the same set, add them to the set and union them
        if find_set(nodes[u]) != find_set(nodes[v]):
            A.add((u,v, w))
            union(nodes[u], nodes[v])
    # return A
    return A

# Prim's algorithm that takes in verts, a graph, and a start node
def prim(verts, graph, start):
    # Nodes dict that will hold the verts as keys and the nodes as values and heap 
    nodes = dict()
    heap = MinHeap()
    # Go through the verts and make a node for each and add it to the heap with inf as the key
    for vert in verts:
        nodes[vert] = Node(vert)
        heap.add(vert, float('inf'))
    # Start is the start node so decrease the key to 0
    start = nodes[start]
    heap.decrease_key(start.value, 0)
    

    # While the heap is not empty
    while heap.heap != []:
        # Set u to the min and go through the adjacents of u
        u = heap.min()
        for v in graph.adj[u[0]]:

            # Find the weight of the node (not the most efficient but it works for this case)
            for key, weight in heap.heap:
                if key == v[0]:
                    break

            # If the node is in the heap and the weight is less than the current weight, set the parent to u and decrease the key
            if v[0] in heap.current_elements and v[1] < weight:
                nodes[v[0]].p = u[0]

                heap.decrease_key(v[0], v[1])
        
    # Ans set that will hold the edges of the MST
    ans = set()
    

    # Go through the nodes and if the parent is itself, skip it (elminates the root which is a,a)
    for elem in nodes:
        if elem == str(nodes[elem].p):
            continue

        # Go through the adjacents of the node and if the parent is the edge, add it to the set with the weight
        for node, weight in graph.adj[elem]:
            edge = nodes[elem].p
            if node == edge:
                ans.add((elem, edge, weight))
                break
    # Return the set
    return ans

    




def main():
    # Verts and edges
    verts = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    edges = [
        ('a', 'b', 4),
        ('a', 'h', 8),
        ('b', 'c', 8),
        ('b', 'h', 11),
        ('c', 'd', 7),
        ('c', 'i', 2),
        ('c', 'f', 4),
        ('d', 'e', 9),
        ('d', 'f', 14),
        ('e', 'f', 10),
        ('f', 'g', 2),
        ('g', 'h', 1),
        ('g', 'i', 6),
        ('h', 'i', 7)
    ]

    # Edges are sorted by weight
    edges = sorted(edges, key= lambda x: x[2])

    # Graph object that holds the verts and edges
    graph = Graph()
    graph.v = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    # Add each edge to adj by first adding all the verts as keys with an empty set as the value and then adding the edges to the set
    for vert in verts:
        graph.adj[vert] = set()
    for edge in edges:
        graph.adj[edge[0]].add((edge[1], edge[2]))
        graph.adj[edge[1]].add((edge[0], edge[2]))
    
    # Call the two functions
    output_kruskal = kruskal(verts, edges)
    output_prim = prim(verts, graph, 'a')

    # Print the output with the sums
    print(f"Edge set of kruskal algorithim (order may be different): {output_kruskal}")
    print(f"Total weight of Kruskal: {sum([x[2] for x in output_kruskal])}")
    print(f"Edge set of Prim algorithim (order may be different): {output_prim}")
    print(f"Total weight of Prim: {sum([x[2] for x in output_prim])}")

main()
