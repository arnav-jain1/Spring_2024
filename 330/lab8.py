class Graph:
    # Graph holds verts and edges as dicts for easy and quick access. 
    def __init__(self) -> None:
        # For vert, the key will be the letter and the value will be the node object
        self.v = dict()
        # For edges, the key will be the vert and the value will be a set of its edges
        self.adj = dict()

class bfsnode:
    # Node object with default vals as per the slide (-1 instead of inf)
    def __init__(self) -> None:
        self.color = 'white'
        self.d = -1
        self.p = None

# Same as bfsnode but with default as 0 and f var for finished time
class dfsnode:
    def __init__(self) -> None:
        self.color = 'white'
        self.d = 0
        self.f = 0
        self.p = None



def bfs_func():
    # All verts and edges according to graph 1
    bfs = Graph()
    vert = {"s", "t", "u", "v", "w", "x", "y", "z", "r"}
    edges = {("s", "r"), ("s", "u"), ("s", "v"), ("t", "u"), ("t", "r"), ("y", "u"), ("y", "v"), ("r", "w"), ("v", "w"), ('w', 'z'), ("x", "y"), ("x", "z"), ('x', 'w')}

    # FOr each node, add it to the dict and create it's key (with value as an empty set) in the edges dict
    for node in vert:
        bfs.v[node] = bfsnode()
        bfs.adj[node] = set()

    # For each edge, add both directions (undirectional) of the edge to the respective key (adjacency list but as a set instead)
    for edge in edges:
        u, v = edge
        bfs.adj[u].add(v)
        bfs.adj[v].add(u)
    
    # Call the search function with the graph and 's' as the starting node
    bfs_search(bfs, 's')



# bfs search where graph is the graph object and S is the starting letter
def bfs_search(graph, s):
    # Initialize the queue and set the starting values then append the starting letter
    queue = []
    graph.v[s].color = 'gray'
    graph.v[s].d = 0
    queue.append(s)

    print(f"Starting with {s}, depth is 0")

    # While the queue is not empty
    while queue:
        # Pop the queue and set it to uletter variable
        uletter = queue.pop(0)
        # U is the actual node of the uletter variable
        u = graph.v[uletter]
        
        

        # Go through all of u's adjacencies 
        for vletter in graph.adj[uletter]:
            # Set v to the actual node of the letter
            v = graph.v[vletter]

            # If the color of v is white, set it to grey, increase the distance by parent + 1, and set parent to u. then appened the letter to the queue and print it
            if v.color == 'white':
                v.color = 'grey'
                v.d = u.d + 1
                v.p = u
                queue.append(vletter)
                print(f"Discovered {vletter}, depth is {v.d}") 
        # Set the color of u (parent) to black
        u.color = 'black'


def dfs_func():
    dfs = Graph()
    verts = {'u', 'v', 'w', 'x', 'y', 'z'}
    edges = {('u','v'), ('u','x'), ('x','v'), ('v','y'), ('y','x'), ('w','y'), ('w','z'), ('z','z')}

    for node in verts:
        dfs.v[node] = dfsnode()
        dfs.adj[node] = set()
    
    for edge in edges:
        u, v = edge
        dfs.adj[u].add(v)
    global time
    time = 0

    def dfs_visit(uletter):
        global time
        u = dfs.v[uletter]
        time = time + 1
        u.d = time
        u.color = 'grey'
        for vletter in dfs.adj[uletter]:
            v = dfs.v[vletter]
            if v.color == 'white':
                v.p = u
                dfs_visit(vletter)
        time = time + 1
        u.f = time
        u.color = 'black'
    
    for u in verts:
        if dfs.v[u].color == 'white':
            dfs_visit(u)





    

bfs_func()
dfs_func()