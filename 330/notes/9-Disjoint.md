# Disjoint sets
* Set: Collection of numbers/elements
* Disjoint if two sets have nothing in common
	* I.E $x_{1} \cup x_{2} = \emptyset$  
## Disjoint-set (Union-find) data structure
* Maintains a collection of disjoint sets
* Each set has a representative which is used to identify the set (chosen element is arbitrary) 
### Operations
Make-set(x): Create a new set with whose only member (and rep) is x
Union(x,y): Merge x and y
Find-set(x): Return the representative of the set with x
