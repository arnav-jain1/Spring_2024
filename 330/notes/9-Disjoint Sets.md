# Disjoint sets
* Set: Collection of numbers/elements
* Disjoint if two sets have nothing in common
	* I.E $x_{1} \cup x_{2} = \emptyset$  
## Disjoint-set (Union-find) data structure
* Maintains a collection of disjoint sets
* Each set has a representative which is used to identify the set (chosen element is arbitrary) 
### Operations
Make-set(x): Create a new set with whose only member (and rep) is x
Union(x,y): Merge x and y
Find-set(x): Return the representative of the set with x
Scenario:
	Make-set is called n times to create n sets with 1 element
	m operations of UNION and FIND-SET are performed (m - 1 unions)
Important for finding connected components of an undirected graph or minimum spanning tree of a weighted graph

### Linked List representation
Each set has its own linked list with elements of the set (order doesnt matter)
Set object points to tail and head
Each set has two pointers, next and set pointer (points back to set object)
Representitive of each set is the first element of each list
Essentially a singly linked-list of linked-lists
![[Pasted image 20240320105115.png]]

<mark style="background: #FF5582A6;">MAKE-SET(x)</mark>: Create a new linked list with element x $\theta(1)$
<mark style="background: #FF5582A6;">FIND-SET(x)</mark>: Follow the pointer from x to the set object then return the object that the head points to. <mark style="background: #ADCCFFA6;">$\theta(1)$</mark>
<mark style="background: #FF5582A6;">Union(x,y)</mark>: Append y's list to end of x and update all of the pointers (the ones pointing to the set). $\theta(len(y))$ because all of y has to be updated
	This union always appends the second element to the first
	If there are n elements and you are always appeneding longer list to the shorter one (worst case), then it is $\theta(n^2)$ because each element is appeneded n times.
<mark style="background: #FF5582A6;">Weighted-Union(x,y)</mark>: Always appends shorter list to the longer one
	.<mark style="background: #CACFD9A6;">	O(nlogn)</mark>


### Tree Representation 
Each set is a rooted tree where each node is an element
Each node has one pointer which points to parent (root points to itself and is representative)
![[Pasted image 20240320111311.png]]

<mark style="background: #FF5582A6;">MAKE-SET(x)</mark>: Create a new tree with element x $\theta(1)$
<mark style="background: #FF5582A6;">FIND-SET(x)</mark>: Follow pointers from x up to the tree root $\theta(d)$ d = depth
	In the picture, FIND(e) returns c and find(g) returns f
<mark style="background: #FF5582A6;">UNION(x,y)</mark>: Makes root of second tree (y) point to root of first (x)
	Runtime of $\theta(max(d_{1}, d_{2}))$ where $d_{1}$ and $d_{2}$  are depths of x and y because it takes $\theta(d)$ do FIND-SET 
	![[Pasted image 20240320112219.png]]
	This always makes second point to first so if you had m UNION (and thus m FINDSET), the worst case is a linear line thus making the total runtime O(mn) or O(n^2)
<mark style="background: #FF5582A6;">Union by rank</mark>: Root of tree with smaller rank (depth) points to root of tree with higher rank
	Rank is increased by 0 or 1
	Find-set and union is O(logn)  because that's the depth so the total runtime is O(mlogn)
<mark style="background: #FF5582A6;">Union by size</mark>: Instead of keeping track of depth you keep track of amount of nodes. the root of the tree with less nodes points to the root of the tree with more nodes
	Both work well but in practice rank is easier


## Path Compression
In FIND-SET, Path compression makes each node in the path to the element point to the root
![[Pasted image 20240320113919.png]]
Total runtime for Union by rank and path compression is $O(m\alpha(n))$ where $\alpha(n)$ is a really slow growing function so the time complexity is essentially (but not technically) O(m) (linear)
![[Pasted image 20240320172957.png]]

