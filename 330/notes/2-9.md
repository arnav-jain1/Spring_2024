# Heap
## Heap
Array that can be viewed as a binary tree
Each row is filled except the last row

Parent index = i // 2
Left child = 2i
Right child = 2i + 1

Height: logn

Max_heap: Largest element at the top (root), parent always more than children
Min_heap: Smallest element at the top (root), parent always less than children

### Max Heapify
Recursive procedure that maintains the max_heap property
![[Pasted image 20240209094540.png]]
Running time is O(logn) because you do it for each level in the height

Build max heap calls max heapify for every element
![[Pasted image 20240209094804.png]]
Runtime is O(nlogn) but a tighter analysis says that it is O(n) since it isn't called for half the leafs

## Heapsort
Makes a heap based on an unsorted list
![[Pasted image 20240209111008.png]]
**Loop Invariant** At the start of each iteration, A\[1:i] is the smallest i elements while A\[i+1:n] is the n-i largest elements in sorted order

Worst case runtime: O(nlogn) because to build the heap you have to iterate n times and to heapify it is logn so to build the heap the runtime is nlogn

# Comparison sort
Sort elements by comparing the two numbers
Includes: insertion, merge, quick, heap
Other forms exist like counting sort, radix sort, and bucket sort

Any comparison sort algo has a worst case runtime of $\Omega(nlogn)$ 
	Heapsort and merge sort are asymptotically optimal because their worst case is O(nlogn) unlike the others whose worst case is $O(n^2)$ 


# In place sorting
Algorithm is called in-place if the input array is directly sorted and a new one doesn't need to be created they have $\theta(1)$ additional space so it has space efficiency
	Insert
	Heapsort
	Quicksort (needs O(n) or O(logn) additional space in memory for recursive calls)
Out-of-place algorithms require a new array to be created for the sorted elements thus needing $\theta(n)$ extra space to sort an array

# Priority queue
Application of heap (both min and max) with 4 functions:
	1. Insert(element, key): adds an element O(logn) because heapifying takes logn and adding an element takes O(1) ![[Pasted image 20240212162348.png]]
	3. Max/min(): returns the max/min value $\theta(1)$ ![[Pasted image 20240212165330.png]]
	4. extract(): returns and removes max/min value $O(logn)$ because need to heapify ![[Pasted image 20240212165445.png]]
	5. Increase-key(element, num): Increases the value of element x's key to num $O(logn)$ since it takes logn to heapify and assuming O(1) to find the elem ![[Pasted image 20240212162204.png]] 

Ex: *Scheduler*: Scheduling jobs on a computer with different deadlines/priorities
	Heap keeps track of jobs to be executed and their priorities
	When a job is finished it grabs the next task by doing extract()
	When a job is pending for a while you can do Increase it
	Can add an additional job by doing insert
	