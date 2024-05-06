# Dynamic Programming
Design princple optimization problems
Examines multiple choices at each step and chooses the one that leads to the global optimal solution
Also involves solving subproblems

3 problems:
	Rod cutting
	Matrix chain multiplication 
	Longest common subsequence

## Rod cutting
Problem: Company buys long steel rods and cuts them into shorter rods
	Long rod has length n (integer)
	Short rod is $1 \le i \le n$ and sells for $p_i$
	Each cut is free
	Find best way to cut rod to max revenue
![[Pasted image 20240502212058.png]]
Exhaustive search would be $O(2^{n-1}) = O(2^n)$, dynamic programming would be $O(n^2)$ 
Lets say n = 4, then 3 possible cutting positions so $2^{3}= 8$  ways

You can find the optimal revenue recursively by getting optimal revenue of sub problems
![[Pasted image 20240502213230.png]]
If you implement it, it has $\theta(2^n)$ because it keeps calling CUT-ROD repeatedly 
![[Pasted image 20240502213311.png]]
Dynamic Programming solves this by solving each subproblem once and then saving the solution, so if you need it later you can get it.
Two ways:
	Top-down approach 
	Bottom-up approach

### Top-down approach (with memoization)
Similar to pseudocode but with checks to make sure the subproblem hasn't already been solved, if its solved then get the result, if not then continue normally 
![[Pasted image 20240502214204.png]]

### Bottom up
Depends on the the fact that the bigger problem is made of subproblems
Solves the smaller subproblems first and uses the smaller subproblems to build the bigger one
Note: Usually iterative 
![[Pasted image 20240502214640.png]]
Lines 1-2 initialize, line 3 goes over every possible length up til the one we are trying to find. Line 4 sets q very low. Line 5-6 goes thru every possible cut. Line 7 sets r to the max and line 8 returns
$\theta(n^2)$ due to doubly nested loop (so is top down)
	Bottom up has better constant factors since it isn't recursive 
	Sometimes top-down is better when you don't need to try the subproblems
### Subproblem Graph
![[Pasted image 20240502214815.png]]
Shows how subproblems depend on each other
Node is a subproblem, arrow is a dependency
Top down is top to bottom while bottom up bottom to top

![[Pasted image 20240503152943.png]]
![[Pasted image 20240503153130.png]]
Edited code to add where to cut instead of just the maximum revenue

## Matrix-chain multiplication
Input: Sequence of rectangular matricies $\{A_{1},A_{2}, ..., A_{n}\}$  and a sequence of dimensions $\{p_{0}, p_{1}, ... , p_{n}\}$ where matrix $A_{i}$ has dimension $p_{i-1} \times p_{i}$  
Output: Find parenthisization that minimizes total number of scalar multiplications when done using the standard algorithm (triply nested loops)
![[Pasted image 20240503153840.png]]

Parenthesization is an order in which matricies in the chain are mult together
Since Multiplication is associative, it yields the same final product but different amount of computations (what we are trying to minimize)
![[Pasted image 20240503154007.png]]

Example: Let dimensions of $A_{1} = 10 \times 100$ , $A_{2} = 100 \times 5$, and $A_{3} = 5 \times 50$  
	$A_{1}A_{2} = 10*100*5 = 5000$ and $A_{1:2}A_{3} = 10 * 5 * 50 = 2500$ so $(A_{1}A_{2})A_{3} = 7500$ computations
	Doing $A_{1}(A_{2}A_{3}) = 100 * 50 * 50 + 10 * 100 * 50 = 75000$  computations
To find the most optimal parenthesization exhaustively it takes $\Omega(2^{n})$ time 
![[Pasted image 20240505151509.png]]
### Recursive 
Let $A_{i:j}= A_{i}A_{i+1}...A_{j}$ 
Let m\[i,j] denote the min number of scalar multiplications to get $A_{i:j}$  
Suppose the optimal parenthesization between $A_{k} and A_{k+1}$ 
![[Pasted image 20240503161514.png]]
Where p... is scalar mult to compute combining both sides

But since the optimal algorithm at the top level is unknown, we have to try all values of k between i and j so this is the new formula:
![[Pasted image 20240503161650.png]]

Also, let s\[i,j]=optimal value of k that achieves the minimum m\[i,j] 
s will be used to construct the parenthesis like above
Then the optimal solution would be 
	m\[1:n]: Min scalar operations
	s\[1:n]: location of top level parenthesization
### Dynamic
Imagine an ixj table, the algorithm fills up that table bottom up
	Since i $\le$ j, only half the table needs to be filled up
The subproblem size is j-i+1 (m\[2:4] is size 3 because $A_{1}A_{2}A_{3}$)
First, main diagonal filled with 0s (no computation for $A_{1}$)
![[Pasted image 20240503183523.png]]
filled from lower diagonal -> upper diagonal
Final solution is given by m\[1,n] ![[Pasted image 20240503183635.png]]
Essentially it wants the min of adding two subproblems and then the cost of combining for all the subproblems
![[Pasted image 20240503185543.png]]
	Line 1 makes the tables and line2-3 puts 0s in first diagonal
	Line 4 gets the diagonal
	Line 5 and 6 help get the coordinate and 7 sets to inf
	Line 8 tries every possible cut and if the cut is the smallest, store it and remember the index
Run time is $O(n^{3})$ since 3 nested for loops
s is n-1 by n-1 because the first row is all 0s 
![[Pasted image 20240503185954.png]]
the m table is the total number of operations to do $A_{i}A_{j}$ so $A_{1}A_{6}=15125$ 
The s table is what k would be so for $A_{i}A_{j}$, k = 3 (split up to A1A3 + A4A6) 

Compute m\[2,5] and s\[2,5]
![[Pasted image 20240505153040.png]]
s\[2,5] means k = 3 so s\[2,3] and s\[4,6]. since 2,3 is just two matricies you dont simplify that. s\[4,6] = 5 so $(A_{2}A_{3})((A_{4}A_{5})A_{6})$ 
![[Pasted image 20240503191357.png]]
s\[1,1] = 1 so just $A_{1}$
s\[1,3] = 1 so s\[1,1] and s\[2,3] so $A_{1}(A_{2}A_{3})$ 
s\[1,6] = 3 so s\[1,3] and s\[3,6]. s\[1.3] = $A_{1}(A_{2}A_{3})$ and s\[4,6] = 5 so s\[4,5] and s\[6,6] so $(A_{1}(A_{2}A_{3}))((A_{4}A_{5})A_{6})$ 

Note: Multiplication doesn't actually happen, n refers to matricies being multiplied
## Longest common subsequence
Finds longest subsequence that is common between two given sequences to measure similarity (like DNA)
For a given sequence X = $\{x_{1}, x_{2}, ... x_{n}\}$, Z = $\{z_{1}, z_{2}, ... ,z_{m}\}$  is called a subsequence if the characters in Z are in same order but not necessarily consecutive in X
![[Pasted image 20240503193452.png]]
The goal is to find the maximum length common subsequence of both X and Y (may not be unique)

Example X = {A,B,C,B,D,A,B} and Y={B,D,C,A,B,A}
	Z1 = {B,C,A} is a common subsequence but not longest
	Z2 = {B,C,B,A} is longest
	Z3 = {B,D,A,B}
	No common length of 5

Exhaustive runtime:
	All possible subseq of X is $2^n$, checking if it is a subseq of Y takes linear time m so runtime is $O(2^{n}m)$ 

### Recursive sol
$X_{1}$ has length i and $Y_{j}$ has length j and c\[i,j] has is the length of the LCS
Idea: Compare the last characters of Xi and Yj and then recurse. 
Case 1 xi == yj:
	Recurse by finding LCS of $X_{i-1}$ and $Y_{j-1}$
	LCS = (LCS(Xi-1, Yj-1, xi)   
	Length: c\[i,j] = c\[i-1, j-1] + 1
Case 2 $x_{i} \ne y_j$  
	Recurse by finding LCS of $X_{i-1}$ and $Y_{j}$ 
	LCS = (LCS(Xi-1, Yj)   
	Length: c\[i,j] = c\[i-1, j]
Case 3: Same as case 2 but drop $y_{j}$
	Recurse by finding LCS of $X_{i}$ and $Y_{j-1}$ 
	LCS = (LCS(Xi, Yj-1)   
	Length: c\[i,j] = c\[i, j-1]

We usually need to find the max of Case 2 and case 3
![[Pasted image 20240504141023.png]]
Note: LCS uses a condition to restrict which subproblem to consider
Also, there is another table b\[i,j] to track which case leads to the value of c\[i,j] above
Length of LCS is c\[m,n]


### Dynamic Programming
Fills up a table of size c\[0:m,0:n] using bottom up approach 
The first set where i=0 or j=0 is filled with 0s
![[Pasted image 20240504141530.png]]

Every c\[i,j] depends on a square one up, one left, or one upper left
	c\[i-1,j] or c\[i,j-1] or c\[i-1,j-1] 
	![[Pasted image 20240505154244.png]]
So you can fill up the table in any order that respects the dependencies 
	row-major order: 1 row at a time bottom to top
	Can do column, or diagonal (kind of) but not used as much
c\[n,m] gives the optimal solution (bottom right corner)
![[Pasted image 20240504142335.png]]
The runtime is $\theta(nm)$ since there are n\*m entries and computing each takes constant time
![[Pasted image 20240504142857.png]]
The arrow traces the optimal solution back to the base case
![[Pasted image 20240504142943.png]]
if equal:
	diagonal + 1
else:
	if up >= left:
		up
	else:
		left
# Dynamic Programming
Must have two elements to apply
	Optimal substructure: the globally optimal solution has subproblems with optimal solutions (greedy algorithms)
	Overlapping subproblems: Space of subproblem is actually small and recursive subproblem just solves same problems multiple times rather than unique subproblems (essentially, the problem solves the same thing multiple times which is inefficient because it can be done bottom up and saved to be used later)
![[Pasted image 20240504191614.png]]

You can design a DP solution according these steps:
1. Prove optimal substructure: Show that the optimal solution has subproblems with optimal solutions themselves (skipped in class)
2. Provide recursive formulation: Get precise formula to optimal solution value which is based on the optimal solution to subproblems
3. Fill up the table: Done in more than one way as long as dependencies are respected. Auxillary table filled up at same time
4. Construct optimal solution: Build the optimal solution by backtracking the auxillary table (print)

Both greedy and DP exploit optimal substructure 

## Knapsack Problem
Problem: A knapsack can carry *W* pounds. The store has *n* items and *i*th item is characterized by 
	$v_{i}$: value
	$w_{i}$: weight
Goal: Decide what items to take to maximize the total value while being lower than W
Application: Selecting TV ads to max rev for a fixed time interval
![[Pasted image 20240504192434.png]]
Two variants
	Fractional variant: Optimal greedy solution
	0-1 variant: can be solved by DP

### Fractional variant
Thief can have a fraction of an item where the weight and price scale accordingly
Thief takes items in order of decreasing value per pound $\frac{v_{i}}{w_{i}}$ until weight is reached
![[Pasted image 20240504193121.png]]
### 0-1 variant
Thief must take full item or no item
Greedy algo doesn't work, dynamic is better
![[Pasted image 20240504193135.png]]


# Paradigms 
Covered 3:
1. Divide and conquer (computational)
	Divide problem into smaller subproblems which are solved recursively (merge/quicksort)
2. Greedy (optimization)
	Select the optimal choice for each subproblem leading to the optimal solution
3. Dynamic Programming (optimization)
	Examine multiple choices that have a subproblem that is shared with other subproblems (generally solved bottom up)
