Created due to issues with SQL
	Not made for distributed computing
	Not every data problem is best with DBMS like find friends of friends of friends...  because this gets expensive

# NoSQL
Not Only SQL
Class of non relational data storage system
	Flexible schema
	Usually no join
	Massive scalability
	Relaxed Acid
	No declarative query language so more programming
## CAP Theorem 
3 properties:
	Consistency 
	Availability
	Partition Tolerance
Can have 2 of the 3
When expanding, you have to partition so you have to chose between consistency and availibility
	Right overlap
	Almost always chose availibility 
![[Pasted image 20240411143956.png]]

Availibility: System that continues to operate even if a node is down in a node system or there is a network disruption between the nodes
Consistency: Nodes M and N having the same info. Not possible with AP because if there is a network disruption but it continues, then how can it be consistent?

Eventual consistency: The idea that if there are no updates, eventually the db will be consistent. For any given update/node, either the node will reach the update or is removed
Known as BASE
	Basically Availible: System essentially always up
	Soft state: Not always consistent 
	Eventually consistent: Becomes consistent later

## Types
2 major types:
	Key/Value aka big hash table
		Very simple, like a dict
		Effecient, scalable, based of keys
		Cons: Many objects can't be molded as key value pairs
	Schema-less which has many types like column based, graph based, etc
MapReduce
	Programming framework for distributed parallel operations
	Map and reduce functions
	Hive- schemas, SQL like language
	Pig- More imperitive but with relational operators
	Both compile to MapReduce job

Graph based:
	Nodes have properties 
	Edges have labels or roles
	Interface varies (recursion, path expression, single-step)
	Give up Join, Order, group, ACID, SQL