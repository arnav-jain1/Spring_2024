# Data Structures
## Sets
Collection of values 
Can be manipulated by algorithms and changed (insert, delete, search, etc)
Attributes of a dynamic set:
	key: used to identify the object 
	Satellite data: Other information about the object that is more general
	Other data: Pointers to other objects
Some dynamic sets assume there is some resemblance of order in a set
Dynamic Sets examples:
	arrays, stacks/queues, graphs, linked lists, skip lists, trees hash tables, disjoint sets

## Set operations
1. Queries: return information about the set
2. Modifying operations: Change the set
Time to do the operation is measured in terms of the set being of size n

## Array
Continues sequence of memory space
Matrix are just two dimensional arrays but they can be represented as one continues block of memory
Single array: more efficient
Multiple array: more flexible 
takes $\theta(1)$ to access any matrix element directly 

### Matricies 
2d arrays, can be represented like 1d array in row major or column major 
Ie if 
$$
\begin{matrix}
1 & 2 & 3 \\
3 & 5 & 6
\end{matrix}
$$

it can be represented \[1,2,3,4,5,6] or \[1,3,2,5,3,6] (column major)
single array is more efficent but multiple array is more flexible. Either way access $\theta(1)$ 
## Stacks/Queues
Dynamic sets where insert and remove is prespecified
Stacks: Last in first out
	Insert is called push 
	Delete is called pop
	Can be implimented with an array that is \[1:n] elements long
	S\[1] is the bottom element of the stack while S\[n] is the top element 
	if stack is full then location of S.top = size
	![[Pasted image 20240505172528.png]]
	![[Pasted image 20240214093010.png]]
	All 3 operations are $\theta(1)$
Queues: First in first out
	Insert is called enqueue
	Remove is called dequeue
	Needs one element of buffer so n -1 can be implemented as S\[1:n]
	Q.head is the start of the queue, next to be removed
	Q.tail is the end of the queue, the last element that was added
	Q.size is the max capacity of the queue + 1
	A queue is circular, it wraps around, so if Q.head == Q.tail == index 1 then it is empty
	Full queue is if the Q.head == 1 and Q.tail position == Q.size or Q.head=Q.tail+1
	![[Pasted image 20240214093805.png]]
	Time complexity is $\theta(1)$ 
![[Pasted image 20240505172823.png]]	
## Linked Lists

Data structure in which elements are in linear order but connected via pointers
Singly Linked list: Each element points to the next element
Doubly linked list: Each element points to the previous and next element

**<mark style="background: #FF5582A6;">Doubly linked list</mark>**
Each element has key and 2 pointers, next and prev
	Next points to successor
	Prev points to predecessor
	If next points to NIL then last, if prev points to NIL then first
	Head points to First element (NIL if empty)
### Searching
Start with the first element and keep doing element.next
![[Pasted image 20240219113806.png]]
$\theta(n)$ time
### Inserting
Prepending (adding to the front) takes $\theta(1)$ time
![[Pasted image 20240219113929.png]]
Inserting (adding anywhere in the list) takes $\theta(1)$ time
Takes element to add and where to add it
![[Pasted image 20240219114037.png]]
![[Pasted image 20240505173212.png]]
### Deleting
Remove an element from a linked list
Takes element that needs to be deleted
$\theta(1)$
![[Pasted image 20240219124520.png]]
![[Pasted image 20240505173242.png]]
## Sentinels
Dummy element that allows simplification of boundary elements 
In linked lists, all NIL elements are replaced by sentinel NIL
![[Pasted image 20240505173308.png]]
It turns a regular linked list circular because both the front and the back are pointing to the same NIL sentinel
Useful because it simplifies the code quite a bit because it reduces edge cases and can sometimes slightly make it faster
![[Pasted image 20240505173330.png]]
![[Pasted image 20240505173350.png]]
If there are many linked lists it is extra space but also very slight speed increase

## Array vs Linked lists
Arrays are easier
Linked lists are more flexible
![[Pasted image 20240219131839.png]]
