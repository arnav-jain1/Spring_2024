# Sql

## Intro
Very high level language, tell what to do not how to do it
DBMS finds best way to execute query (query optimization)
Two sublanguages: 
	DDL: Data definition language- Define and modify schema
	DML: Data manipulation language- Insert/update/remove rows
Responsible for efficient optimization 

# Basics
SELECT $A_{1}, A_{2}... A_{n}$ FROM $R_{1}, R_{2}...R_{n}$ WHERE *condition*
	Aka SPJ (select project join) query 
	Select what is shown in the result (attributes)
	From is where to get the data
	Where is a boolean statement that filters the results
![[Pasted image 20240227143347.png]]
The difference is that relational algebra is on sets while SQL  is on bags
Example: 
	Find all the names of the students that are under 20 years old
	SELECT name FROM Student WHERE age < 20;
	$\pi_{name}(\sigma_{age < 20}(Student))$ 

## Projection
SELECT * FROM student;
Single table query and the WHERE clause is optional
\* is shorthand for all columns
Change column name using AS alias
SELECT sid AS 'ID' FROM student
or 
SELECT sid 'ID' FROM student
AS becomes optional here
or 
SELECT 'ID' as sid From student
String literals are in single quotes

The SELECT list can also have expressions 
	Can use built-in functions like SUBSTR, ABS, etc.
Example:
	Get birth year of students
	SELECT 2024-age FROM student;


Constants can also be used as expressions
Example:
	SELECT 0 AS id, 'Anonymized' AS name, age, GPA  FROM Student
	Here everything in the id column would be 0, everything in the name column would be 'Anonymized' and the rest is the same

## Selection
WHERE condition is a boolean expression that is checked on each tuple
Can use AND to have 2 different expressions

LIKE can be used for string pattern matching

<mark style="background: #ADCCFFA6;">Ask about case sensitivety beacuse I was not paying attention</mark>
## Ordering
ORDER BY *col_name* \[ASC\\DEC]
Sort by ascending or descending order 
Happens after SELECT so you can only order by one the SELECTed columns
ASC is default value
Can use sequence numbers to order, for example you can do ORDER BY 4 to order by the 4th variable in the SELECT

## Select vs Bag semantics
SQL does not remove any duplicates by default 
It saves time and returns the actual distribution
Can do SELECT DISTINCT to get set answer
DISTINCT on entire result not just a single attribute

## Create table creates a new table
CREATE TABLE SHIP (  
	SHIPNUM varchar(3) <mark style="background: #FF5582A6;">PRIMARY KEY</mark>,  
	SHIPNAME varchar(25),  
		DEFAULT 'Titanic'
	BUILDER varchar(20),  
	LAUNCHDATE datetime,  
	WEIGHT int(11),  
		<mark style="background: #FF5582A6;">PRIMARY KEY (SHIPNUM)</mark>
);
This creates a table with column names being the first column and the length of the attribute being the second column
Both highlighted ways work for creating a primary key, the second way can be used to have multiple vars be a primary key
A default value for the table can be specified instead of NULL


You can also create a subtable using a subquery where the contents that satify the subquery are used to make the new table 
![[Pasted image 20240227150147.png]]

## Modification 
Does not return result but changes the table 
1. Insert
2. Delete
3. Update

### Insert
INSERT INTO *relation* VALUES *List of values*
For example:
	INSERT INTO likes VALUES ('Sally', 'Bud');
It is better practice to explicitly list the columns you want the data to go into
	INSERT INTO likes(beer, drinker) VALUES ('Sally', 'Bud');
	This avoids mistakes, autofills NULL, and protects against breaking if the table shape changes
	
### Update
UPDATE *relation* SET *Attributes to be changed* WHERE *Condition*

### Delete 
DELETE FROM *relation* WHERE *condition* 
Deletes the whole tuple so be careful
Can't undo