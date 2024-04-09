# Making a db
<mark style="background: #FF5582A6;">Constraint</mark>: Relationship that dbms is required to enforce
	Ex: key constraint, foreign key, value-based (must be of particular type), tuple-based, assertions
<mark style="background: #FF5582A6;">Triggers</mark>: Executed when a specific condition occurs (like inserting a new tuple)

For a single attribute Key, place PRIMARY KEY or UNIQUE after the attribute name and before the , in the CREATE TABLE method
	Can also put on own line like `PRIMARY KEY(attr1, attr2)` 

## Foreign keys
Values in attributes of one relation must appear in attributes of another relation 
	Ex: In Enroll(SID, CID), SID must associate to a student and CID must associate to a class
To enforce, put `REFERENCES Relation(attr)` after the attribute but before the comma. Note, whatever it references must be a primary key
Can also put at the end (as a schema element) with `FOREIGN KEY(attr) REFERENCES relation(attr)` 

### Enforcement
WIth foreign keys, there are two violations possible Assume R has a foreign key of S
1. Inserting to R where the attr is not in S
	Handled by rejecting the insert/update
2. Deleting/updating in S which leaves R "dangling"
	Handled in 3 ways
	1. Reject the deletion/modification
	2. Cascade, make the same changes in S
	3. set attr of S to NULL 
The Policies can be set when declaring a foreign key with: 
```
CREATE TABLE Sells (
bar     CHAR(20),
beer    CHAR(20),
price   REAL,
FOREIGN KEY (beer)
	REFERENCES Beers (name)
	ON DELETE SET NULL 
	ON UPDATE CASCADE
);
```

## Checks
Add CHECK(condition) to the declaration of the attribute to add a constraint.
Condition can use the name of the current relation's attribute but any other relation/attr used MUST BE IN A SUBQUERY
Example (foreign key reject and price constraint)
```
CREATE TABLE Sells (
bar     CHAR(20),
beer    CHAR(20) CHECK (beer IN (SELECT name FROM Beers)),
price   REAL CHECK (price <=5.00)
);
```
Checked on insert/update only

### Assertion
Defined by CREATE ASSERTION *name* CHECK *condition* (Own command, not with a table)
	Can refer to any relation or attr in the schema
Checked after every modification to ANY relation (clever program will only check if actually affected though)

### Triggers
Attribute-based checks are powerful but get missed sometimes since they aren't always checked
Assertions are inefficient

How triggers work:
	Event: What "triggers" the trigger (Ex: insert on Sells)
	Condition: A boolean expression
	Action: Any SQL statement
Example: Lets say you are adding something to S without adding it to R. Usually it would just error out but with a trigger, you can make it so that it makes a new tuple in R with NULL values
Example:
CREATE TRIGGER BeerTrig (
	AFTER INSERT ON Sells
	REFERENCING NEW ROW AS NewTuple FOR EACH ROW
	WHEN NewTuple.beer NOT IN (SELECT name FROM Beers))
	INSERT INTO Beers(name) VALUES(<mark style="background: #CACFD9A6;"></mark>)
)
The event is the first line
The second line is how to refer to it
Third line is the condition
The fourth line is the action
Notes:
	Can also use CREATE OR REPLACE TRIGGER if you want to modify/are unsure
	Can replace AFTER with BEFORE
	INSERT can be DELETE or UPDATE. UPDATE can be for a specific attribute as well

Triggers are either row-level or statement-level
	FOR EACH ROW specifies row-level, without it is statement
	Row level: Execute once for each tuple
	Statement-level: Execute once for a SQL statement no matter how many tuples are modified
Referencing:
	Insert implies new tuple for row-level or new table for statement level
	Delete implies old tuple/table
	Update can do both
	Can refer to them by 
	`[NEW or OLD] [TUPLE or TABLE] AS <name.`
Condition:
	Must be boolean
	Evaluated on how the tb is before or after triggering the event depending on which word is used BUT it will always be BEFORE THE CHANGES TAKE EFFECT
Action:
	Can have more than one statement (must surround with BEGIN...END) 
	Usually doesn't make sense to do so
	