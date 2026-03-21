#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument. This script is safe from
MySQL injections.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Arqumentləri terminaldan götürürük
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Bazaya qoşuluruq
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    # Cursor yaradırıq
    cursor = db.cursor()

    # Təhlükəsiz üsul: %s yerinə data arqument kimi ötürülür.
    # MySQLdb kitabxanası bu datanı avtomatik təmizləyir (escape edir).
    # Diqqət: Sorğu daxilində %s ətrafına dırnaq işarəsi qoymuruq!
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    
    # execute() metodunun ikinci arqumenti mütləq tuple (və ya siyahı) olmalıdır
    cursor.execute(query, (state_name,))

    # Nəticələri götürürük
    query_rows = cursor.fetchall()

    # Nəticələri çap edirik
    for row in query_rows:
        print(row)

    # Bağlantıları qapadırıq
    cursor.close()
    db.close()
