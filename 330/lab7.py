# Node class
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

# Elems to add
elems = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# Store all of the elems are a dict where the key is the letter and the value is the Node
nodes = dict()
for elem in elems:
    nodes[elem] = make_tree(elem)

# Call the methods in the criteria with the respective Node object
union(nodes['b'], nodes['a'])
union(nodes['d'], nodes['c'])
union(nodes['f'], nodes['e'])
union(nodes['f'], nodes['g'])
union(nodes['c'], nodes['b'])
union(nodes['g'], nodes['h'])
union(nodes['d'], nodes['g'])
find_set(nodes['f'])

# For each element, print the element, parent, and rank.
for elem in elems:
    print(f'Parent of {elem} is {nodes[elem].p} and rank is {nodes[elem].rank}')