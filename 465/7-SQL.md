# Lec 7
# SQL
Domain specific language used to communicate with relational dbs
	Manage stored data 

## SQL Injection
Root cause: Input being interpreted as a SQL command
Usually done by "Injecting" sql query into a web form
Two main types:
	Blind: DB does not give user info after submitting the query
	Non-Blind: User gets info from query

Easiest way (if possible) Use 1 = 1. This is always true so it will give as much info as you can specify

