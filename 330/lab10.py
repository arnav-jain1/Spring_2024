import heapq
# Most of the code below is reused from previous labs
class Graph:
    # Graph holds verts and edges as dicts and sets for easy and quick access.
    def __init__(self) -> None:
        self.v = dict()
        self.edges = {}


# Node object
class Node:
    def __init__(self, value) -> None:
        # Has a value, parent (default is None), and d (default is inf) vars
        self.value = value
        self.p = None
        self.d = float('inf')
    # Str method for printing
    def __str__(self) -> str:
        return str(self.value)
    
# Decrease key function that removes and readds the key to the queue
def decrease_key(queue, v, d):
    # Finds the element, removes, readds
    for elem in queue:
        if elem[1] == v:
            queue.remove(elem)
            heapq.heappush(queue, (d, v))
            break




# New Code


# Relax function that relaxes the edges 
def relax(u, v, w):
    # If the weight of v is greater than the weight of u + w, set v.d to u.d + w and set v.p to u
    if v.d > u.d + w:
        v.d = u.d + w
        v.p = u

# Print true function that prints the path from s to v, takes in a graph, s, v, and a retstring (return string)
def print_tree(G, s, v, retstring = ""):
    # If v is the source, then add it to the return string
    if v == s:
        retstring += s + ' '
    # If the parent of v is None, then raise a runtime error because there is no path
    elif G.v[v].p == None:
        raise RuntimeError(f"No path from {s} to {v} exist")
    else:
        # Otherwise, call the recurse with the parent of v. After recursing add v to the return string
        retstring = print_tree(G,s,G.v[v].p.value, retstring)
        retstring += v + ' '

    # Return the return string for the recursion 
    return retstring

# Weight sum function that takes in a dict of edges and an input string (from print_tree)
def weight_sum(edgesDict, inputString):
    # Clean the input
    inputString = inputString.strip().replace(' ', '')
    # Pair the verts up with the next vert to get the edges
    edges = list(zip(inputString, inputString[1:]))
    sum = 0
    # For each edge, get the weight from the edgesDict and add it to the sum
    for u,v in edges:
        for v2, w in edgesDict[u]:
            if v == v2:
                sum += w
    return sum


# The verts and edges
verts = {'s','t','x','y','z'}

edges = { ('s','t',6), ('t','x',5), ('x','t',-2), ('s','y',7),('y','z',9), ('z','s',2), ('z','x',7), ('t','y',8),
          ('t','z',-4), ('y','x',-3)}
edgesDict = dict()
nodes = dict()
# Initialie vertexes, edges, graph and get all the edges in a dict
for vert in verts:
    edgesDict[vert] = set()
    nodes[vert] = Node(vert)
for v1, v2,w in edges:
    edgesDict[v1].add((v2,w))
graph = Graph()
graph.v = nodes
graph.edges = edges

# Bellman ford fuction that takes in a graph and the source
def Bellman_Ford(G, s):
    # The source distance is 0
    G.v[s].d = 0
    # Go through all the edges and relax them n-1 times
    for _ in range(len(G.v)-1):
        for u,v,w in G.edges:
            relax(G.v[u],G.v[v],w)
    # Go through all the edges and check if there is a negative cycle, if there is return false
    for u,v,w in G.edges:
        if G.v[v].d > G.v[u].d + w:
            return False

    # Otherwise return true
    return True



print("BF: ")
# Call bellman ford and print the path
Bellman_Ford(graph, 's')
for vert in verts:
    # print the path and total weight using the functions for each vertex in the graph
    print(f"Shortest path from s to {vert}: ", end="")
    x = print_tree(graph, 's', vert)
    print(x)
    print("Total weight: " + str(weight_sum(edgesDict, x)))



# Dikstra's Algorithm that takes in a graph, source, and a dictionary of edges
def Dijkstra(G, s, edgesDict):
    # The source is set to 0 and initialize the queue
    G.v[s].d = 0
    queue = []
    
    # For each vertex, push it to the queue
    for vert in G.v:
        heapq.heappush(queue, (G.v[vert].d, vert))
    
    # While the queue is not empty, pop the vertex (get the element at index 1 because 0 has the weight for queue)
    while queue:
        u = heapq.heappop(queue)[1]
        # For each of the adj edges relax them 
        for v, w in edgesDict[u]:
            # If there was a change in the weight of v after relaxing, decrease the key. Cur is used to save the value and check for changes
            cur = G.v[v].d
            relax(G.v[u], G.v[v], w)
            if cur == G.v[v].d:
                decrease_key(queue, v, G.v[v].d)


# Same code as before but different edges
verts = {'s','t','x','y','z'}
edges = {( 's','t',10), ('s','y',5), ('t','x',1), ('t','y',2), ('x','z',4), ('y','t',3), ('y','x',9), ('y','z',2), ('z','s',7), ('z','x',6)}
edgesDict = dict()
nodes = dict()
# Initialie vertexes, edges, graph and get all the edges in a dict
for vert in verts:
    edgesDict[vert] = set()
    nodes[vert] = Node(vert)
for v1, v2,w in edges:
    edgesDict[v1].add((v2,w))
graph = Graph()
graph.v = nodes
graph.edges = edges

print("\n\n")
print("Dijkstra:")

# Call Dijkstra and print the path in the same way as before
Dijkstra(graph, 's', edgesDict)
for vert in verts:
    # otherwise print the path and total weight by calling the same functions as before
    print(f"Shortest path from s to {vert}: ", end="")
    x = print_tree(graph, 's', vert)
    print(x)
    print("Total weight: " + str(weight_sum(edgesDict, x)))