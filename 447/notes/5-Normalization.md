# Why Normalization
Normalization is the process of reducing redudancy in a database
Why? 
	1. It wastes disk space
	2. Insertion anomalies (such as creating a new class that doesn't have any enrollments yet) ![[Pasted image 20240213124025.png]]
	3. Increases likelihood of inconsistencies
	4. Makes it harder to delete specific things
It is better to decompose and take one large table and make it into smaller tables so that it can be updated individually ![[Pasted image 20240213124251.png]]
DO NOT decompose too much to the point where it is redundant yet again such as decomposing the right most table into two seperate labels 
![[Pasted image 20240213124645.png]]
# Functional Dependency 

<mark style="background: #FF5582A6;">Functional Dependency  </mark> (denoted by X --> Y where X and Y are sets of attributes in relation R): If two tuples in R have the same X attribute(s) they must have the same Y attribute(s)
![[Pasted image 20240213125002.png]]
Alt Def: X --> Y means $T_{1}[X] = T_{2}[X] \iff T_{1}[Y] = T_{2}[Y]$  Where X and Y is $\ge$ 1
If X is the same then Y has to be the same

Trivial dependency is if X --> Y and Y is a subset of X
	Ex: (SID, SName, Department) --> SName
Completely non trivial if X and Y have no overlap
Can be partially non trivial if some but not all overlap

## Partial Dependency
Lets say XY is a Candidate Key and Z is a non-key attribute
X --> Z is a partial dependency because Z depends on a part of the candidate key not the full candidate key.

## Keys pt 2
An attribute set is a candidate key if:
	1. They functionally determine all other attributes (It is impossible for 2 of the same attribute sets being the same)
	2. No subset can functionally determine all other attributes of R
Set of attributes that has a key is called a superkey
	Ex: ![[Pasted image 20240213130044.png]]
# Normalization
Normalization: Process of decomposing bad relations by decomposing them into good ones
Normal form: Certification that tells whether the relational schema in a particular state
## First normal form
2 traits
1. It's a table, Every row-column intersection has ONE atomic value
2. Primary key is enforced
	No duplicate rows
	Rows are identified by primary key and columns by attribute name
	Values accessed by primary key of tuple and name of attribute (row and col)
## Second normal form
In first normal form AND Every non-prime attribute is fully dependent on FULL candidate key
	Prime means member of candidate key
	This means that any non candidate key attribute must be tied to the candidate key itself, not a part of the candidate key
	![[Pasted image 20240213135554.png]]
	This is not Second Normal form because account and name has a partial dependency on SID instead of having a dependency on the full candidate key (SID and CID)

## Third Normal Form 
In 2NF form and No transitive dependency
### Transitive dependency 
Lets say A is a candidate key and B, C are not.
Lets say A --> B and B --> C, C is transitively dependent on B 
![[Pasted image 20240215122546.png]]
This is bad because status depends on city so it is not in 3NF
![[Pasted image 20240215122636.png]]
This is done to avoid anomalies (but requires extra computation)
Mainly needed to stop human error
### Potential anomalies
Deletion anomaly such as wanting to delete 3500, that removes New York and domestic which we may want to keep
Insertion anomaly such as wanting to only add a city and status instead of the full thing
Update anomaly like if someone changes 3493 to domestic then there are inconsistencies

## Bryce-Codd Normal Form (BCNF)
In BCNF if:
	For all Nontrivial FD X --> Y, X is a super key 
So for example:
r(X,Y,Z) suppose XZ and YZ are candidate keys
Also suppose X-->Y
This situation is in 3NF because there is no transitive property
It is NOT in BCNF because there is a dependency X-->Y where X is NOT the superkey

# Decomposition 
The process of Turning a large table into smaller tables
1. Lossless join: It is possible to recreate the original table from the decomposed tables
		COunterexample: No way to get original table from the decomposed tables
		![[Pasted image 20240215124433.png]]
2. Dependency Preservation: It should be possible to check in the project relations whether all given FDs are satisfied
	Counter Example: Both subtables are fine but it still doesn't work properly 
	![[Pasted image 20240215124935.png]]
How to decompose into BCNF:
1. Find candidate keys
2. Find a BCNF violation
	Non trivial FD X-->Y in R where X is not a superkey
3. Grow Y to include all attributes determined by X
4. Decompose R into R1 and R2
	1. R1 has attributes X $\u$  Y
	2. R2 has attributes X \u Z where Z has all attributes of R that arent in X or Y (Z = R - X - Y)
5. Repeat
![[Pasted image 20240215124900.png]]

