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
    vert = {"r", "s", "t", "u", "v", "w", "x", "y", "z"}
    edges = {("r", "s"), ("s", "u"), ("s", "v"), ("t", "u"), ("r", "t"), ("u", "y"), ("v", "y"), ("r", "w"), ("v", "w"), ('w', 'z'), ("x", "y"), ("x", "z"), ('w', 'x')}

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
    # Get the graph from the slides
    dfs = Graph()
    verts = {'u', 'v', 'w', 'x', 'y', 'z'}
    edges = {('u','v'), ('u','x'), ('x','v'), ('v','y'), ('y','x'), ('w','y'), ('w','z'), ('z','z')}

    # Add the info to the graph object in the same way as BFS 
    for node in verts:
        dfs.v[node] = dfsnode()
        dfs.adj[node] = set()
    for edge in edges:
        u, v = edge
        dfs.adj[u].add(v)
    
    # Create a global time variable for visit to use
    global time
    time = 0

    # Visit function that takes in a letter
    def dfs_visit(uletter):
        global time
        # set u to be the object that corresponds with the letter
        u = dfs.v[uletter]
        # Increment the time and then set the discovered and color vars then print discovered
        time = time + 1
        u.d = time
        u.color = 'grey'
        print(f"Discovered {uletter}")
        
        # Go through everything it is adjacent to
        for vletter in dfs.adj[uletter]:
            v = dfs.v[vletter]
            # If the node that it is adj to is undiscovered, set the undiscovered parent to the u and visit it
            if v.color == 'white':
                v.p = u
                dfs_visit(vletter)
        # Increment time again and set finished and color vars
        time = time + 1
        u.f = time
        u.color = 'black'

    # Call the visit function with the starting node to be 'u
    dfs_visit('u')

    
    # Go through each vert and if there are any that are undiscovered, call the visit function with them this is where some randomization could happen because verts is a set. z might be chosen first or w
    for u in verts:
        if dfs.v[u].color == 'white':
            dfs_visit(u)

    # Print out the discovery and finished times
    print("Discovery and finish time:")
    for u in verts:
        print(f"{u} was discovered at time {dfs.v[u].d} and was finished at time {dfs.v[u].f}")




# Call the functions
print("BFS search with order and depth:")
bfs_func()
print()
print("DFS search in order of discovery, NOTE: May be a little randomized because after choosing u as its first element it will pick a random one out of the rest")
dfs_func()