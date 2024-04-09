# View
Like a virtual table
Defined by a query so that the contents are able to be seen fast
DBMS stores the query itself 
Can be used in queries 

Example: CREATE VIEW test1 AS SFW...
	The tables in the SFW are called base tables
Then to drop the view:
	DROP VIEW *view_name*
Essentially like setting a query to a variable but the output isn't stored rather the query statement itself is

Views do not have join, aggregation, or subquerries because it leads to ambiguous results

Done to:
	Hide data
	Hide complexity 
	Data independence, 

![[Pasted image 20240402153139.png]]

## Materialize
Can force DBMS to create the tables from the view instead of storing the query 
The created tables behave like ordinary tables so they are faster but need storage
Changing the materialized table does not change the original data
`CREATE MATERIALIZED VIEW`

## Modifying views
Makes sense because users see a view they don't see the dbms
The goal is to modify the base table so it looks like its done on the view too
![[Pasted image 20240402153601.png]]
Modifying the view can modify the base table as well. But note, suppose the view is GPA = 4.0, adding a 3.7 GPA to the view will add it to the base table but it won't appear on the view

# Authorization
A file system has privileges on the objects it manages and it has certain participants to whom they may be granted
Access control specifies WHO can do what OPERATIONS on what DATA
User is referred to authorization ID (login name)
If the ID is PUBLIC then it is available to any authorization ID

There are 9 privileges in total which SQL can grant that include
1. SELECT 
2. INSERT
3. DELETE 
4. Update
To do a query you need ALL of the privileges in the query statement

You can also grant privileges with:
	GRANT *privileges*
	ON *relation*
	TO *IDs*
	.<mark style="background: #BBFABBA6;">WITH GRANT OPTION</mark>
If you want to allow the recipient to pass the privileges add the green line (without the .)
To remove, replace GRANT with REVOKE
	REVOKE only works for the GRANT you did. So if they were granted priviledge elsewhere, they will still have it
	Adding CASCADE removes all GRANTs passed down
	RESTRICT will fail if the privilege has been passed down

Priv can be granted to view instead of base table to prevent access to data

## Nodes
Nodes are how privaleges are kept track of
SELECT ON R and SELECT(a) ON R live on different nodes
Edge x -> y means node X granted Y
AP is used for ID A having privilege P
	P* is with grant option
	P** is the source of the privilege 
	Draw an arrow between the two nodes with arrow pointing to who it was granted to
	If granting a subprivilege (Update(a) instead of update) then replace P with Q
![[Pasted image 20240402162937.png]]
If revoking, delete the edge
If trying to REVOKE with restrictAP->BP and BP has an edge elsewhere, it fails and no changes
There always has to be a path from the user to the source
	If one of the edges in the path is deleted, all subsequent are as well
![[Pasted image 20240402163206.png]]
