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
## Primary 