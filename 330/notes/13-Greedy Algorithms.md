# Optimization Problems
How to max/min certain objective
	Ex: MST, shortest path
	Many possible solutions, interested in the optimized (max/min) sol
	Called *an* optimal solution instead of *the* optimal solution

Greedy algorithm makes the best choice at each step (makes locally optimal solution to try to get globally optimal solution)
	Doesn't always work but usually does


# Activity selection (scheduling)
Problem: Schedule competing activities that use the same resource (like cpu)
Rules:
	Set S is a set of all activities 
	The resource can only do one activity at once with a start $s_{i}$ and finish $s_{f}$ where $s_{i} \le s_{f} \lt \infty$  so the range is $[s_{i},s_{f})$ 
	Two activities are compatible if their ranges dont overlap
Goal: Minimum subset *A* of S
![[Pasted image 20240428210709.png]]
## Greedy choice
Decision to pick the activity is to select the one that will finish earliest
This will allow the resource to be as free as possible and a smaller subproblem to be created
![[Pasted image 20240428210856.png]]
Runtime: $\theta(n)$ because each activity is examined once and examining takes $\theta(1)$ time. Though this assumes sorted list, otherwise $\theta(nlogn)$ because you need to sort first

# CPU Scheduling
Problem: Scheduling different jobs multiple times on a single machine to minimize total completion time
Rules:
	Set S is a set of all jobs
	The machine can only do one job at once where $j_{i}$ is the job and $c_{i}$ is the completion time
Goal: Have a processing order that minimizes total completion time
![[Pasted image 20240428211907.png]]
## Greedy choice
Pick the shortest processing time first because it lowers the waiting time of the rest of the jobs. YOu then have a smaller subproblem
Called the shortest job first algorithm (SJF)
1. sorts all the jobs in increasing order of $c_i$ 
2. Schdeules them one after another
If already sorted then $\theta(n)$ otherwise $\theta(nlogn)$ 

# Greedy algorithms
Essentially, they make the most optimal choice to create a smaller subproblem to apply the same logic
For Greedyness to apply there must be 2 elements
1. Greedy-choice property
	Optimal choice at each iteration
2. Optimal substructure 
	The globally optimal solution has an optimal solution to a subproblem (essentially the backwards of 1)
### Steps
1. Cast the optimization problem: Essentially make the problem fit the framework of optimal choice -> subproblem ->  repeat
2. Prove greedy choice: SHow there is always an optimal solution that uses the greedy choice so the greedy choice is ALWAYS safe (requires math/proofs)
3. Prove optimal substructure: Show if you combine the optimal solution with the greedy choice that's made, you get to the optimal solution (skipped because intuitive)

# Huffman code
Lossless data compression technique where data is a sequence of chars
Input: table with how often each char occurs (frequency)
Output: Optimal way of storing each char has a binary bit string (code word)
Goal: Represent it using the least number of bits
![[Pasted image 20240428214540.png]]
Fixed length code: Each codeword is same length. Need $logn$ bits 
Variable length code: Each codeword can be different length where infrequent characters have longer codes and freq ones have smaller codes
	Prefix-free code: No code is a prefix for another code so decoding is unambiguous 
	Huffman is variable length and prefix free

## Binary tree
Prefix-free coding scheme can be represented via BT where each leaf is a char
The codeword is obtained by going from the root to the leaf where each left is a 0 and each right is a 1
![[Pasted image 20240428215212.png]]
![[Pasted image 20240428215221.png]]
Each node is the total amount of chars in its subtree
## Huffman code
Optimal variable length, prefix free code that minimizes bits *B(T)* to encode a file
Huffman's algorithm builds the tree in a bottom-up manner using a greedy algo

It starts with a set of chars that are merged to create the final tree
At each step, the two least frequent chars (By min priority Q) are summed and merged 
Merge reduces number of objects one by one to create a subproblem that is solved similarly
![[Pasted image 20240428215634.png]]
![[Pasted image 20240428215707.png]]
Time complexity is $\theta(nlgn)$ because extract and insert take $\theta(lgn)$ and you do that n-1 times so n\*lgn