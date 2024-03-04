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

#
