# Hash Table (dict)

Supports dictionary operations (Insert, delete, Search)

Assume:
	Each element has a unique key and other data (like a row in a db)
	If the size of the hash table is m, the hash table is size T\[0:m-1]

## Direct addressing
Works well when universe of keys (all usable keys) is small 
Suppose Universe of keys U = {0,1,2,...m-1}
Each slot corresponds to key in the univ
	T\[key] points to satellite data
	T\[key] points to nil if there is no key k
Insert, delete, search is all O(1)
The downside of this is that if U is super large, then it becomes impractical with too much wasted space since keys needed could actually be pretty small 
![[Pasted image 20240304113319.png]]

Ex: KU IDs (7 digit num). The universe of keys is 10,000,000 (10^7) but that much space isn't needed and most of it would be wasted

## Hash table
More effecient when set of actual keys is much smaller than the universe of all possible keys
Size of hash table is m = O(n)
Uses hash func to compute slot number
![[Pasted image 20240304113255.png]]

### Collision
Happens if 2 keys go to the same slot
Hash tables try to avoid this by choosing a good hash function or resolving collisions if they do occur
Ideal hash function will have an equal probability to hash into each slot for any given k. It is random, uniform, and independent

Hash table with the ideal function is called independent uniform hashing
	Hard to implement so we aprox to the ideal

# Hash Schemes
## Static hashing
Single, fixed hash function so the same input will be hashed to the same spot
Very vulnerable to worst case behavior

Worst case $\theta(n)$
Average case: $\theta(a)$ where $a=n/m$ which is the load factor or number of elements in each slot

### Division method
h(k) = k mod m
Works well when m is a prime number
Many keys can hash to the same slot so like if m = 7 then 8, 15, 22 all hash to 1
### Multiplication method
$h(k)=\left\lfloor m (kA\mod 1) \right\rfloor$  where  0 < A < 1
The mod 1 removes the integer part so like 4.5 % 1 = .5 and the floor then removes the fraction
m does not need to be prime


## Random hashing
Introduce randomization to reduce collisions
Family of hash functions {h1, h2,...hn} are used
If you have 2 keys k1 and k2, h1 will hash k1 and h2 will hash k2 but any malicious adversary will not know which one is used
$\theta(a)$
### Universal hashing
Special case of random hashing
Family of hash functions is called universal if it satisfies the universality property:
	For distinct k1 and k2, the amount of hash functions that will put them in the same spot is <= |H|/m
	If we randomly pick h from H and the probability that h(k1) = h(k2) is 1/m
![[Pasted image 20240304124819.png]]

## Perfect Hashing
Perfect hashing guarantees 0 collision
Only works for an unchanging set of n elements 
Simple and two-level schemes used

### Simple Scheme
Performs following procedure to remove collision
	1. Construct hash table of $n^2$
	2. Chose a universal family of H hashing functions
	3. **LOOP**
		1. pick a function $h \in H$ uniformly at random
		2. Use h to hash n elements into the table
	4. **UNTIL** No collision for the n elements
Trial are the steps in between LOOP and UNTIL
~2 trials to find success

### Two level Scheme
Two-level perfect hashing has two levels of tables with universal hashing at both levels
First level is m=n (collisions exist)
Second level has different sizes for each slot in the first level so collisions don't exist
	Second level size of first level + square of the collided elements
![[Pasted image 20240304133822.png]]

# Collision reduction

Even with good functions, multiple elements could go to the same spot
2 techniques to reduce:
	Chaining
	Open addressing

## Chaining
Use linkedlist for all elements that hash to the same slot
slot n points to the start of the linked list or NIL
![[Pasted image 20240308190139.png]]
In this case, insert/delete take $\theta(1)$ time
Worst case search is $\theta(n)$ (all elements hash to the same spot)
Average search is $\theta(1+a)$ where a is the load factor 

## Open addressing
Stores all elements in the hash table itself
Each entry only has one element or nil
Load factor can never be >1
Collisions handled by continiously probing (going through) different slots of the table
	Insert: Keep going (probing) till an open spot is found
	Search: Keep going until an the element is found (success) or empty spot (fail)

For each key *k*, a probe sequence, h(k,i), is used
	1. h(k,0)
	2. h(k,1)
	3. h(k,2)
	4. h(k,3)
	5. ...
	Example:
		Lets say you are trying to insert 10. h(10,0) = 2 but key 2 is already taken so then you do h(10,1)= 5 which is also taken. Then h(10,2)...you continue until all spots are checked or an empty spot is found.
![[Pasted image 20240308191230.png]]


### Probing
Probing strategy has a hash function h(k,i) where k is the key and i is the probe number


#### Linear probing
$h(k,i) = (h_{1}(k) + i) \mod m$ where $h_{1}(k)$ is the hashing function
This allows the function to go to the next position and then wrap around until i == size of table 
![[Pasted image 20240308191640.png]]
It is easy to implement but also leads to clusters which slows everything down


#### Double Hashing
$h(k,i) = (h_{1}(k) + i*h_{2}(k)) \mod m$   Where h1 and h2 are both auxillary hash functions
	Note: m is prime and h2 returns a val < m
	If h2(k) = 1, it becomes linear probing
Probe sequence:
![[Pasted image 20240308191958.png]] ... mod m
![[Pasted image 20240308192038.png]]
### Runtime
Assumes:
	Uniform hashing: Each key is equally likely
	Load factor < 1: # elements < # slots
Unsuccessful search: 
	Worst case: $\theta(n)$ searches all slots
	Average case: $\frac{1}{1-a}$, if a is constant then $\theta(1)$ 
Successful search: More complex but faster since it usually means it isn't there if it is taking long

Insert: Same time as unsuccessful search because finding empty slot
Delete:
	Takes $\theta(1)$ but tricky because search might depend on the element
	You sometimes have to mark it is DELETED so search continues but the load factor is messed up then
<mark style="background: #FFB86CA6;">Another way is to rearrange the table after the delete so that the elements don't depend on a vacated space and the load space is still applicable</mark>
![[Pasted image 20240308192713.png]]
	
