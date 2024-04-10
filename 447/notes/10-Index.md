# Motivation
Cost of binary search on dbs can be high
multiple types of searches:
	Equality: WHERE A = y
	Range: WHERE A > Y

Tree structured indexing techniques: Support range and equality searches 
ISAM (Index sequential access method): Static structure, early index technology

## Index file
File that contains keys and pointers that point to the data file to do binary search 
Sometimes, the index file is still too big so you need to split the data file into index blocks which contain blocks of data
![[Pasted image 20240409104602.png]]
So to look up 202, you go to the second index block which has 202 as a data block. Kind of like a skip list

Update:
	When adding, add an overflow block below the datablock
	When deleting, remove from the datablock
	This degrades performance
	When updating, do both
Outdated idea, B+- trees used instead
Used until v5.4

# Database indexing concepts
## Dense vs Sparse indexes 
Dense: One index entry for each search key value
	Each entry has its own ID
	Faster, better for smaller data
	Can directly tell if exists or not
Sparse: One index entry per block 
	Records clustered according to the search key
	Each index refers to a block rather than a specific key
	Better for larger datasets 
	Records must be clustered 
	Easier updates
	![[Pasted image 20240409105200.png]]
## Primary vs Secondary Index
Primary Index:
	Created for primary key of table
	Can be sparse
Secondary Index:
	Usually Dense
	Created for unique 
	Can be created on non-key attribute
	Ex: <mark style="background: #BBFABBA6;">CREATE INDEX GPAIndex ON STUDENT(GPA)</mark>
There can be multiple secondary indexes but only one primary

Recap
Primary index: index structure for primary key of a file that is sorted according to primary key
![[Pasted image 20240409155303.png]]
Secondary index: structure built for non-key attribute that is sorted according to primary key
![[Pasted image 20240409155311.png]]

# B Tree

Tree based index file: Can be primary/secondary, sparse/dense, clustered/unclustered 
Hierarchy of intervals
![[Pasted image 20240409155520.png]]
Height constraint: All leaves at same lowest level
Fan-out constraint: All nodes (except root) at least half full
degree (d): min keys an interior node can have
![[Pasted image 20240409160521.png]]
![[Pasted image 20240409155740.png]]
Like a BST but slightly more complex

When adding to a node that is full, you have to propogate up 
	When it goes to the root, and the root is full, there is a new root of fan out 2 and the tree grows upwards
If deleting from a tree, you either have to steal or merge with another leaf. Make sure to change the ancestor if doing so

## Time
How many operations?
	h the height of tree
	+1/2 for manipulation
	Plus O(h) for reorganization if need be
	-1 if cache the root
How big is H?
	$log_{fan-out}{N}$ where N is the number of records
	B+ tree properties say that fanout is at least d/2 for all non-root nodes
	Fanout is usually very large
	4-level tree is usually good

COmplex reorganization usually not implemented 
	Less than half full is okay
Most Use b tree

## Endless update
<mark style="background: #BBFABBA6;">UPDATE Payroll  SET salary = salary * 1.1 WHERE salary >= 100000 </mark>
This went on infinitely because it would keep finding itself. 
Solution was to create a "to-do" list so each was only done once