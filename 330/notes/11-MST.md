# Free Tree
Graph that is undirected, Connected, and acyclic.
	If it is unconnected, then it is a forest
Free tree always has these properties:
	Two verts connected by a unique simple path (path where all verts are distinct)
	E = V -1
	If any edge is removed, then the graph is unconnected 
	If any new edge is added, then there's a cycle

## Spanning tree
In a graph that is connected and undirected, a spanning tree is a free tree that has all the verts in the original graph as well as a subset of edges

# Weighted graph
Connected undirected graph with a weight function that has the cost of each edge
The MST is a spanning tree with the least total cost in the set A of edges
	May not be unique
The minimum spanning tree *T* has the same vertex set as the graph so it is only represented by the edge set 
![[Pasted image 20240401111918.png]]

## Finding MST
Kruskal's algorithm and Prim's algorithm
Both are greedy algorithms (make local optimal decisions) and guarentee finding the MST

### Generic method
Cut:
	Cut (S, V-S) is a partition of G's vertex set into two disjoint subsets S and V-S
	Ex: Orange and tan verts
Cross:
	An edge *$(u,v) \in E$*  is a cross if one of its edges points to S and the other points to V-S
	Ex: (a,h)
Respect: 
	A cut respects a set of edges *F* if no edge in set F crosses the cut
	Ex: The cut respects the set of blue edges
![[Pasted image 20240401200952.png]]
Start with empty tree and grow the MST by adding one "safe edge" at a time
Safe edge (all reasons must be satisfied):
	There is a cut that respects the MST so far
	(u,v) is an edge that crosses the cut and the weight of it is the least along all edges crossing the cut
	Ex edge 7
![[Pasted image 20240401201153.png]]

### Kruskal's algorithm

The edge set *A* is a forest (collection of trees)
At the start A is empty and forest is V singleton verts
All edges are processed in an increasing order of weight
Each iteration finds the edge that connects two trees with the lowest weight

Implemented using a disjoint set
	Each set is a tree in the forest 
	Trees gradually merged to form MST
	The set is sorted by weight and processed one by one
![[Pasted image 20240402100835.png]]
Run time is dominated by sorting 
$O(E * log(V))$


### Prim's algorithm 
Always maintains one tree that will grow to form the MST
Starts with arbitrary root vertex
In each iteration, the tree adds the minimum weight edge that connects it to a vertex not a part of the tree already
This process is repeated until there are no more verticies not a part of the MST

Implementation:
	Min heap for verts not in the tree with insert, remove, and decrease-key functions (logv)
	Each vert has two vars
		v.key: Minimum weight of any edge connecting v to the tree (set to inf and gets updated when a neighbor is added to the tree)
		v.p: Parent of v when added to the tree (initially NIL)
	![[Pasted image 20240402103338.png]]
	Runtime is O(E * logV) Because you have to decrease each vert (logV) after each edge is added. (lines 10-14)
	