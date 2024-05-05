# Graphs
Represent set of objects where some pairs are of objects are connected
G = (V,E)
	V = Vertex Set with all Verticies/Nodes
	E = Edge Set with all edges (connections between nodes)
Runtime is measured by size, |V| = numbers of vertices and |E| = Number of edges
Directed or Undirected graphs

# Terminology
## Adjacency 
Given an edge (u,v), u is <mark style="background: #FF5582A6;">adjacent</mark> 
	If the graph is undirected, the adjacency relation is ALWAYS symmetric
	If the graph is directed, the adjacency relations is sometimes symmetric (1,2 and 2,1 for symmetry)

## Degree
The degree of a vertex is the amount of edges connected from/to it
	If the graph is undirected, It is the number of vertex connected to the node
		The sum of degrees is double the amount of edges
	If the graph is directed:
		The <mark style="background: #FF5582A6;">in-degree</mark> is the number of edges entering the node
		The <mark style="background: #FF5582A6;">out-degree</mark> is the number of edges leaving the node
		Degree is the sum of the two
![[Pasted image 20240328134357.png]]
Left figure: Node 2 has degree 2
Right figure: Node 2 has in-degree 2, out-degree 3, degree 5

Lemma: If a graph is undirected, the sum of the degrees of all verts is 2\*number of edges

# Directed Graph (Diagraph)
The edge set E has a set of directed edges
	(u,v) means u goes to v
	$(u,v) \ne (v,u)$ 
	(u,u) is a self loop 
![[Pasted image 20240328133558.png]]
Adjacency-list representation:
	Array of |V| elements where each element is a vertex and points to a linked list of all the verticies it is adjacent to
	Total length of all linked lists is |E| 
	Storage: $\theta(V + E)$
Adjacency-matrix representation:
	Same as directed graph
	Not always symmetric though
	Storage: $\theta(V^2)$
![[Pasted image 20240328141327.png]]
# Undirected graph
Each edge goes both ways
Adjacency-list representation:
	An array of |V| elements where each element is a vertex and points to a linked list of all of the verticies it is adjacent to 
	Total length of the linked lists is 2*# of edges (|E|)
	Storage: $\theta(V + E)$
	Number of verts + edges which checks out 
Adjacency-matrix representation 
	|V| \* |V| matrix where all numbers are 0 unless there is an edge which then it becomes 1
	Symmetric for undirected 
	Storage: $\theta(V^2)$
![[Pasted image 20240328140155.png]]


# Weighted Graphs
Graph but each edge has an associated weight
Adjacency-list representation: 
	Each element of linked-list stores the weight as a var
Adjacency-matrix:
	Each element of matrix stores the weight ($\infty$ if not adjacent)

# Graph search
Searching a graph involves following the edges to visit all the vertices 
Discovers structure of graph 
2 algortithms:
	Breadth-first Search (BFS): For minimum spanning trees and shortest path
	Depth-first Search (DFS): For topological sort and strongly connected components 
	
## BFS
Given a graph, a source vertex *s* is chosen arbitrarily and every edge of the graph is explored to discover every vertex *v* reachable from s
The distance (smallest number of edges) from s to every v is computed
Supposed to "expand the frontier" between discovered and undiscovered vertices 
![[Pasted image 20240328151813.png]]
Vertices discovered in waves from source until all verts are found
Wave 1 = all verts with distance 1 from s, Wave 2 = all verts with distance 2 etc
SINGLE FIFO Queue to keep track of the frontier of the waves

### Implementing
White nodes: Undiscovered nodes, all start as white
Gray nodes: Vertex discovered for first time (in frontier) 
	Vertex changed from white to gray
	Enqueued
Black: Vertex is behind the frontier
	Changed when dequeued 
	Followed by discovering all neighbors 
When a white vertex *v* is discovered from a grey vertex *u*, u is the predecessor/parent of v
BFS has 3 attributes for each vertex
* v.color: Color of vertex (default white)
* v.d: Distance from source vertex (default $\infty$)
* v.p or v.$\pi$: parent vertex (default NIL)
When discovered for the first time, v.color = grey, v.d = u.d + 1, v.p = u
![[Pasted image 20240328153414.png]]
Run time is $\theta(V+E)$: Lines 1-4 take $\theta(V)$, lines 12-16 take $\theta(E)$ 
Each vertex is enqueued once and dequeued once (why $\theta(V)$) 
![[Pasted image 20240505000037.png]]
![[Pasted image 20240505000053.png]]

## DFS
![[Pasted image 20240505000655.png]]
Starts from any index and searches deeper before backtracking to search for other vertices, kind of like a BST print
Uses same 3 colors 
	White: Undiscovered
	Grey: DIscovered for the first time
	Black: Finished, All neighbors in adjacency have been completed and explored
2 timestamps are also stored to be used later
	v.d: When first discovered (colored grey)
	v.f: When finished (colored black)
	v.d < v.f
![[Pasted image 20240505000943.png]]
![[Pasted image 20240505001002.png]]
![[Pasted image 20240328155105.png]]
Psuedocode: 
![[Pasted image 20240328155129.png]]
Running time: $\theta(V+E)$ 1-6 in DFS Once per visit so $\theta(V)$ and 5-6 in visit is $\theta(E)$ 


# Paths and cycles
In a directed graph , 
	Path: length of a sequence of verts that are connected by edges
		Path (1,2,4,5) with length 4
	Cycle: A path where the first and the last element are the same
		Note: must have 1 edge in the path
		Cycle: (1,2,4,5,1)
![[Pasted image 20240328164908.png]]

<mark style="background: #FF5582A6;">Directed acyclic graph (DAG)</mark>: Directed group with no cycles

# Topological sort
Linear ordering of all vertices of a DAG so that if there is an edge (u,v) then u appears before v in the ordering
Note:
	Sort for a DAG ONLY
	Not the same as other sorting algorithms

Used to sequence tasks with dependencies 
![[Pasted image 20240505001822.png]]

DFS can be used to do it in $\theta(V+E)$ time
![[Pasted image 20240328165353.png]]
Verts will appear in the reverse order of finish times (v.f)
Intuition: If a vertex is finished (colored black) then all of its dependencies must be finished (colored black)

# Connected components
(undirected graph)

A vertex is <mark style="background: #FF5582A6;">reachable</mark> if there is a path from another vertex to itself
Connected component: Subset of vertex set in which all verticies in the subset are reachable from each other
Connected: Only one connected component G = V where G is the connected component

## Method 1: Graph search
1. BFS/DFS starts with some vertex s and discovers all verts discoverable by s thus making a connected component 
2. If there are more verts t, discover all verts reachable by t creating another connected component
3. Repeat
$\theta(V + E)$ same as BFS/DFS

## Method 2: Disjoint Set 
3 methods: Make-set, find-set, and union
1. Algorithim makes a new set for each vertex
2. Merge the sets for each edge
3. Repeat till all sets are found
$\theta(V+\alpha(V)E)$ where $\alpha(V) \le 4$ for most graphs (find-set time complexity)
![[Pasted image 20240328170739.png]]
