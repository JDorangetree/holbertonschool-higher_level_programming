#!/usr/bin/python3
"""script that lists all states with a name
 starting with N (upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    my_name = argv[1]
    my_pass = argv[2]
    my_db = argv[3]
    db = MySQLdb.connect(passwd=my_pass, db=my_db,
                         user=my_name,
                         host="localhost", port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE states.name LIKE 'N%' "
              "ORDER BY states.id ASC;")
    a = c.fetchall()
    for row in a:
        print(row)

    c.close()
    db.close()
