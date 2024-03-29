# Relational ALgebra
You can do operations on data to filter
Query languages: Allow manipulation and retrieval of data from a database (not a programming language)
	No complex calculations or inferences
	Meant to be easy, simple, and effecient 

Relational algebra: More operational, useful for representing execution plans
Relational Calculus: Let users describe what they want instead of how to compute it (declarative)
These together make up SQL

## Operators
Core set:
	Selection, projection, cross product, union, difference, and renaming
Additional:
	Join, intersection, etc
Unary operators:
	On single vars usually
	On records: selection 
	On columns: projection
Binary operators
	Requires 2+ columns
	Union, intersection, difference, cross product, join

### Projection
Input: table R
Notation: $\pi_{L}$
	L is a list of columns in R
Purpose: Select columns to output
Output: The same rows but only the specified columns
Essentially just shows the specific columns of a table with duplicates removed

### Selection
Input: Table R
Notation: $\sigma_{p} R$
	p is called the selection condition or predicate, all output must satisfy p
Purpose: Filter rows according to a criteria 
Output: Same columns but only the Rows that satisfy p
Essentially just show the rows that make p true where p is a condition(s) from the columns 
![[Pasted image 20240220125106.png]]

### Renaming
Input: Table R
Notation: $\rho_{S} R$ or $\rho_{(A_1, A_2, \ldots)}$ or $\rho_{S(A_1, A_2, \ldots)} R$ 
Purpose: Rename row or table
Output: Same table just with different names

### Union
Input: 2 Tables R and S
Notation: R $\cup$ S
	Must have same schema
Output: A table with all rows in R and S without duplicates 

### Difference
Input: 2 tables R and S
Notation: R - S
	Must have same schema
Output: All rows in R not in S with same schema

### Intersection 
Input: 2 tables R and S
Notation: R $\cap$ S
	Must have same schema
Output: All rows in S and R
Aka: R - (R - S) or S - (S - R) or R * S

### Cross product
Input: 2 tables R and S
Notation R x S
Purpose: Pairs Rows from two tables
Output: For each row in R (r) and S (s) output a new row rs (concat r and s)
Note: Operation is commutitive because ordering of rows is unimportant
if both have an attribute a, R x S will have two attributes with the same name which is not allowed so it is denoted R.a and S.a
![[Pasted image 20240220130200.png]]

### Theta Join
Input: Two tables R and S
Purpose: Relate rows from two tables according to some criteria
Notation: $R \bowtie_{p} S$  
Output: For each r and s, output rs if r and s satisfy p
Essentially cross product then selection

### Natural Join
Input: Two tables R and S
Notation: $R \bowtie S$ 
Purpose: Relate Rows from tables and enforce equality and eliminate one copy of common attributes
Shorthand for: $\pi_{L} (R \bowtie_{p} S)$ 

## Build complex operations
Operators must follow precedence rules 
Three notations:
1. Sequence of assignment statements
2. Expressions with several operators
3. Expression trees
Renaming is very useful for example
	$R_{3} = R_{1} \bowtie_{p} R_{2}$ can be written as $R_{4}= \times R_{2}$ and $R_{3} = \sigma_{p} R_{4}$

![[Pasted image 20240220185950.png]]
1. Selection, projection, renaming
2. Cross product, Natural join
3. Intersection
4. Union, difference
### Expression Trees
Leaves are operands (vars or relations)
Interior nodes are operators applied to what they connect to
![[Pasted image 20240220190531.png]]

## Turing Machine
Relational algebra is not supposed to have recursion but SQL still does
Turing machines are not used because optimization becomes undecidable

# Bag
Bag is like a set but duplicates are allowed
Every set is a bag but not every bag is a set
SQL is a bag language 
Many operations (like projection) are faster on bags than sets
Every operation is used the same way except without duplicates

## Bag Union
Element appears the sum of the number of times it appears in set A and B
	Example: {1,2,1} ∪ {1,1,2,3,1} = {1,1,1,1,1,2,2,3}

## Bag Intersection
Element appears the minimum amount of times it appears in either set
	Example: {1,2,1,1} ∩ {1,2,1,3} = {1,1,2}

## Bag difference
Element appears the difference (a-b) but never less than 0
	Example: {1,2,1,1} – {1,2,3} = {1,1}.

## Laws
Bag laws =/= set laws
Commutative law holds but
S$\cup$S = S
if S is a set but 
B$\cup$B != B
Because if B = {1} then B$\cup$B= {1,1}