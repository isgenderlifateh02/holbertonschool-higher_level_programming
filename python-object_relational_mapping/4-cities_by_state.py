#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
Results are sorted in ascending order by cities.id.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    cursor = db.cursor()
    
    # JOIN istifadə edərək şəhərləri və onlara uyğun ştat adlarını çəkirik
    query = "SELECT cities.id, cities.name, states.name \
             FROM cities \
             INNER JOIN states ON cities.state_id = states.id \
             ORDER BY cities.id ASC"
    
    cursor.execute(query)
    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
