# Trees
Data structure without linear relationships
Each node of a tree is an object with a value and a pointer
2 types of trees:
	Binary tree: each node has at most 2 children
	Unbounded trees: Each node has any number of children

## Depth vs Height
<mark style="background: #FF5582A6;">Depth</mark>: Simplest path from root to the node
<mark style="background: #FF5582A6;">Height:</mark>: Longest simple path from node to a leaf
![[Pasted image 20240505175519.png]]
# Unbounded tree
3 different pointers:
	x.p points to parent node
	x.left-child points to the left-most child (not necessarily left child)
	x.right-sibling points to the node to the right (not right child but literal right node)
![[Pasted image 20240505175610.png]]
# Binary Trees
Each node has 3 pointers
	x.parent points to parent node (if NIL then root)
	x.left points to left node (if NIL then no left child)
	x.right points to right node (if NIL then no right child)
There is an additional T.root that points to the root of the tree

## Binary Search Trees
Binary tree where for every node, the left subtree is smaller and the right subtree is bigger
### tree walk
All tree walks Take $\theta(n)$  since it is called twice for each node and each call is $\theta(1)$ 
<mark style="background: #ADCCFFA6;">In Order</mark>
We can print the BST in order using a recursive algorithm
![[Pasted image 20240219133509.png]]
<mark style="background: #ADCCFFA6;">Pre order</mark>
Print, left, right
Used for recreating the same subtree
<mark style="background: #ADCCFFA6;">Post order</mark>
Left, right, Print
Used for deleting the subtree

### Searching
Searches for a given key by going left or right from the current node starting from the root
O(h) (h is height) time because worst case is a linear tree, $\theta(logn)$ is average case like a binary search
![[Pasted image 20240219151810.png]]
Recursion is more intuitive but Iteration is more efficient

### Min/Max
Searches for min or max of a tree by going left until no more or right until no more
Same time complexity as above

### Successor/Predecessor
O(h) running time
For any given node x, 
	Successor is the next node in the <mark style="background: #FF5582A6;">IN ORDER TREE WALK</mark>
		Done by finding the min (leftmost node) in the right subtree OR (if RST DNE) climb up the tree until the first right turn
		![[Pasted image 20240219152628.png]]
	Predecessor is the prev node in the <mark style="background: #FF5582A6;">IN ORDER TREE WALK</mark>
		Done by finding the max (rightmost node) in the left subtree OR climb up until go left
		In fig below, change right to left, min to max
		![[Pasted image 20240219152844.png]]
### Insert
Insert a new key by tracing a simple path down following the normal rules
O(h) worst case and $\theta(logn)$ average
![[Pasted image 20240219153026.png]]

### Delete
Deletes node from tree with 3 cases
1. No left child: Replace node with its right child (could be NIL)
![[Pasted image 20240505180231.png]]
2. If there is a left child and no right child, replace with it's left chld
![[Pasted image 20240505180318.png]]
3. If there is both children, find z's successor (min in RST) and replace z with it
![[Pasted image 20240505180456.png]]
![[Pasted image 20240505180531.png]]
and recurse
![[Pasted image 20240505180701.png]]
Runtime: $O(h)$ since everything is $\theta(1)$ except Minimum


## Runtime of BST
O(h) for all operations where h is the height
Thus best case (balanced) is $h = \theta(logn)$  
Worst case (linear) is $h=\theta(n)$ 

Balanced trees:
	AVL trees: heights of two child subtrees differ by at most 1
	Red-black tree: Each node has a color bit (red/black) to reorg and balance tree
![[Pasted image 20240505181006.png]]

### Rotation
Balanced Trees have them to  maintain h = logn and BST property
![[Pasted image 20240505181058.png]]
Any modifying operation must have them so that it is balanced (somtimes >1) 
![[Pasted image 20240505181210.png]]

