DBMS Project
Omar Mohammed 
Arnav Jain

Intro: 
Our scenario (mini world) is the NBA. Our mini world describes the relationship between players, their teams, and player stats. It will also include cities around the US and information about them

Requirements Analysis:
Our data will be pulled from the publically available 2022-2023 regular season NBA player stats. 
NBA players each have a position, player ID, age, name, field goal percentage, 3 pointer percentage, minutes played, and other stats
NBA teams each have a win count, name, conference, color, home city, and abbreviation. 
The cities will have the name, state, if they have an NFL team or not, if they have an NBA team or not, and whether they are in the US or not.
We also want to be able to see which players were deemed an all star for that year.

Constraints:
Team abbreviation must be 3 letter string 
State must be a 2 letter string
Win count, age, games, games played, and games started are integers
Position must be a string from the array: \[C,PF,SF,SG,PG\]
Points per game (PPG), field goal percentage(FG%), 3 point percentage(3P%), and the other per game statistics must be floats 
No numeric value can be negative 
pid is a primary key along with city and team name
is_allstar, in__usa, all_star, has_nba_team, has_nfl_team are all bools where 1 is true and 0 is false 
The team attribute in table 'Players' is a foreign key to abrv in 'Team'
The city attribute in table 'Team' is a foreign key to the name attribute in 'City'


Operations:
Get all of the teams with all stars and how many they have
Gets all city/state with nfl and nba team
Gets all cities and their states with multiple nba teams
Select the name, position, age, team, and points ppg of the highest scoring player
Get the average points per game for each position group
Get the average ppg for each conference
 
Relational Schema (Normalized):
\[*italics* denotes primary keys\]

Players(*pid*,name,pos,team, fgp, 3pp, games_started, games_played, ftp, reboundspg, pointspg, turnoverpg, assistspg,stealspg,blockspg, is_allstar)
Team(*name*,abrv,wins,conference, city,color)
City(*name*, state, has_nba_team, has_nfl_team, in_usa)


Note: pg stands for per game; fgp, 3pp, and ftp stand for field goal percentage, 3 point percentage, and free throw percentage respectfully


Implementation:
The database was implemented using MariaDB on the KU cycle servers. It was connected to the html web page using php. 
In order to test and make sure everything was okay, we used the console and debugger tab in our browser to make sure the database was connected.
Then, we tried various queries and made sure they matched when putting them in MariaDB directly. 
We only used php, html, and MariaDB. There was no code that was imported.
In order to turn the ER to a database, we decided to consolidate all star and make it a true/false var of the table 'Player'

ER Diagram:

![[Pasted image 20240417215917.png]]