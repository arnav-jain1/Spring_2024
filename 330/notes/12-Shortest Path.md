# Shortest path
Shortest path between two verts (not neccessarily unique)
Input is a weighted directed graph

Path: Sequence (arr) of verts such that there is an edge between each pair of consecutive verts
weight: Sum of weights of the respective edges

Single-source Shortest-path (SSSP): finds the shortest path from a source vertex to every other vertex of the graph
	Gives you the <mark style="background: #FF5582A6;">Single Pair shortest path (SPSP)</mark> for all verts
	SPSP and SSSP have same worst case runtime
All pairs shortest path (APSP): Finds the shortest path between every pair of verts in a graph

3 algorithms 
1. Bellman-Ford: Works general case, graph has cycles and negative values
2. DAG: Edges can be negative but no cycles
3. Dijkstra: Edges must be positive, can have cycles
All 3 use adjacency lists
Sol representation: Each vertex has two vars
	d: total weight from the source to the current vert
		Originally set to inf
		start set to 0
	p: parent, previous vertex
		original set to NIL
![[Pasted image 20240411170713.png]]

Sol construction: 
	Shortest path weight for any vertex from source is v.d
	shortest path itself is done via backtracking 
![[Pasted image 20240411170908.png]]

Relaxation:
	Used to update attributes of the verts if going with a different route is more efficient
![[Pasted image 20240411171411.png]]

## Bellman Ford
Works with negatives and cycles
Returns true or false:
	True if there are no negative weight cycles in the graph, also returns SSSP solution (v.d and v.pi for every vertex)
	False otherwise 
Used to detect negative weight cycles
![[Pasted image 20240411172110.png]]
Line 1 takes $\theta(V)$, Lines 2-4 take $\theta(VE)$ Because $\forall v \in E$ it calls relax E times and lines 4-8 take $\theta(E)$

## DAG
Does not work with cycles (negatives are fine)
DAG is more efficient because Because it makes 1 pass of edge relaxations instead of V-1

1. Topological sort of verts 
2. Edge relaxations over the verts with 1 pass through

![[Pasted image 20240411172908.png]]

## Dijkstra
No negative weight edges

Uses BFS's waves from source to find all other verts
First time a wave arrives at a vertex *v*, a new wave is started from v
Shortest path is the shortest time for a wave to go from the source to that vertex
	Recall BFS has FIFO queue
	Dijkstra has priority queue

At any time:
	Set *S* has the verts where the shortest path from the source is already determined
	Min priority queue *Q* has verts whose shortest paths haven't been determined yet (based on v.d)
At each step
	Moves highest priority vertex from Q to S
	Relaxes all verts adj to u (starting a wave)
![[Pasted image 20240411174307.png]]
Runtime: $\theta(E\log(V))$ 

# Summary

| Algorithm    | Runtime            | Constraints       |
| ------------ | ------------------ | ----------------- |
| Bellman-Ford | $\theta(VE)$       | None              |
| DAG          | $\theta(V+E)$      | No Cycles         |
| Dijkstra     | $\theta(E\log(V))$ | No negative edges |
