DBMS Can be accessed by many users at a time
DBMS can't allow processes to interact with each other
Not all DBMS are transactional 
	InnoDB is, MyISAM is not

Example:
	T1: BEGIN A=A+100, B=B-100 END  
	T2: BEGIN A=1.06*A, B=1.06*B END
	But how do we know T2 begins right after T1? 
	What if A=A+100 then A=1.06A, then B=1.06B then B=B-100? Then the bank loses money
	This must not happen

The storage engine only cares about what data is read/written
Transaction: A sequence of read/write operations

# ACID
When many users are working at once, Each user has their queries grouped into transactions and they should not interfere with each other. It runs as if it is the only one on the server

**A**tomicity: All transactions happen or None happen
	Rolled back if crashed in the middle of a transaction
	Implemented using logging
**C**onsistency: Transactions are consistent
**I**solation: Transaction must appear to be executed in a sequential order
	Ideally, only the operations that are disjoint are executed together
	Those that are not disjoint are executed sequentially
**D**urability: If a transaction commits, its effects stay

# Transactions
START TRANSACTION 
*Operation*
COMMIT \[ or ROLLBACK\]
Transaction automatically started when a user executes a SQL Statement (implicit)

COMMIT will keep the transaction and write it to the disk
ROLLBACK aborts the transaction like nothing happened
Allows admin to easily cancel all the changes
Statements in concurrent transactions do not see changes until committed 
	If Bob and ALice are working on a table, Bob cannot see Alice's data until comitted

# Isolation levels
Suppose Alice runs min and max on a db while Bob runs delete and ins
	In a non transactional db, the steps can be executed in this order: max del ins min
	leading to inconsistencies 
	In a transactional db, Min and max are grouped so there is no inconsistency either before or after the updated table

Either Alice sees the transaction before Bob's or has to wait until Bob's is done which can be a problem because Bob's can take forever

Isolation levels are choices about what interactions with other concurrent transactions are allowed
	Only affects what you see
If there is only one level, then it is an ACID transaction

SET TRANSACTION ISOLATION LEVEL X WHERE X =
1. SERIALIZABLE
	SEE db before or after other transaction runs depending on when it was started, but never in the middle
	Always consistent but may miss changes 
![[Pasted image 20240409125412.png]]
2. REPEATABLE COMMITTED
	Only see others commited data. If commit in between the two then may be inconsistent
![[Pasted image 20240409125534.png]]
3. REPEATABLE READ
	Like Repeatable read but everything that was read the first time will be there no matter what. 
	Leads to phantom tuples
	Pretty much old + inserts
![[Pasted image 20240409125726.png]]
4. READ UNCOMMITTED
	Reads data that are uncommitted and may never be committed 