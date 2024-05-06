# Randomized algos

## Hiring problem

* You are running an employment agency where you get sent a candidate a day for n days
* You interview and if they are better (ie higher) you immediately hire and fire the old one
* Cost to interview is Ci and cost to hire is Ch assume Ch > Ci
* Total Cost: O($C_{i}n+C_{h}m$)
![[Pasted image 20240205091230.png]]
Worst case ex1 so hiring cost is O($C_{h}n$)
### Probabilistic analysis
Assume random order
We have to enumerate all possible inputs, get running time, get average
	Difficult to apply
We can also use indicator random variable
	Analyze the average contribution to each member of the input to the total running time/cost and then sum it up
	Converts probability to expectations
![[Pasted image 20240205092056.png]]	

For candidate i= n, P(getting hired) = 1/i since theres a 1/i chance that it is bigger than the previous element
![[Pasted image 20240205093813.png]]
Therefore the time complexity for average case hiring is $c_{h}logn$

![[Pasted image 20240505164547.png]]

## Analysis of randomized algorithim
* Probabilistic analysis of a deterministic algorithim
	* Input is random
	* Always same running time
	* Average case running-time
* Randomized algorithim
	* Input is anything and then we randomize
	* Expected running time over input
	* Randomizing is O(n)

How to permute? Uniform random permutation. Go thru each index and swap it with a random index
# Quicksort

Divide: Partition A into 2 subarrays such that all elem A\[mid:] $\le$ A\[mid] and A\[:mid] $\ge$ A\[mid]
Conquer: Sort by recursing
Combine: No need since it is in place
![[Pasted image 20240207111355.png]]
Partitioning: Selects the pivot point and rearranges the elements of the array between the pivot point (less is to left, more is to right)
![[Pasted image 20240207112035.png]]

![[Pasted image 20240505165043.png]]
![[Pasted image 20240505165052.png]]
![[Pasted image 20240505165106.png]]
## Time complexity
Depends on partition
If the list is completely unbalanced the sorting time is $\theta$(n^2) because the amount of recursion is n (one recurse has 0 the other has n-1)
Best case is  is $\theta$(nlogn) because the partitioning is even so it recurses logn times:
$T(n) = 2T(\frac{n}{2}) + \theta(n)$   => master method => $n^{\log_{2}2} = n^{1}= n$ => case 2 => $\theta(n*logn)$ 
Average case is also the same. We can use indicator random variable to get a random list and avoid the worst-case
Can use median of multiple numbers as the pivot number if needed 

Can also randomize list or randomize the partition