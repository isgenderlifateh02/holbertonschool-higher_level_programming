-- Lists all cities of California that can be found in the database hbtn_0d_usa
-- Results are filtered by state_id of California (id = 1)
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
