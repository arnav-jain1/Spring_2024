# Lec 2

## History of DBMS

### 60s

* Created because lots of unknown interactions such as two people saving at the same time, power going out while saving, etc. \
* DBMS built on top of the OS \
* Data is indpendant of access program 

* Goals:
    * Allow users to create their own databases and specify schemas
    * Allow users to query and change data
    * Support lots of data
    * ALlow data recovery
    * Allow many people to access the data at once

* Heirarchical model
  * Each parent can have inf children but each child can only have one parent
  * Very complex
  * No standardization
  * Used records
* Network model

### 70s

* New IBM tables saying to always make two dimentional tables
* Data independence
  * Physical and logical implementation is different
    * Data = relations
    * operations = relational algebra
* relations vs records arugment
  * CODASYL cons
    * Too complicated
    * No formal underpinning 
    * can't manipulate certain quaries
  * Relational cons
    * Not as effecient
    * Too much math



## Codasyl explained
* Essentially, its like a filing cabinet organized in a super specific way. You get a bunch of records from each query and then you keep going through each query to get the information you want

## System R
* <mark style="background: #FF5582A6;">System R</mark>First ever relational dbms
* Ingres: Berkley
* Included many features
  * SQL
  * Query Processing 
  * Views
  * etc

## SQL
* Ingres implemented Quel
* System R implemented Structured Englished Query Language (SEQUEL) 
* Oracle V2: First commercially available SQL implementation
  * Based on System R

## Relational Model
* Relational Algebra
* Relational Calculus
  * Tuple relational calculus
  * domain relational calculus
  * Same thing

## NoSQL
* Problems with SQL:
  * Not good for large scale web-apps
  * Don't need perfect real time consistency always (googling)
* NoSQL = Not only SQL
* Example: Social networks
  * Friendships graphs would make a huge table
  * Query: Find all friends of friends of friends of ... 
    * Would take forever in SQL since hard to optimize
* 3 major papers contributed to NoSQL
  * BigTable (google)
  * Dynamo (Amazon)
  * CAP Theorem