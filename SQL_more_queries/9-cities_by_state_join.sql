-- Lists all cities in hbtn_0d_usa, joined with their state
SELECT cities.name, states.name 
FROM cities 
INNER JOIN states ON cities.state_id = states.id 
ORDER BY cities.id ASC;
