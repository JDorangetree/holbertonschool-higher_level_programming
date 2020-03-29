#!/usr/bin/python3
"""aists all cities from the database hbtn_0e_4_usa"""

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
    c.execute("SELECT cities.id, cities.name, states.name FROM cities "
              "INNER JOIN states ON cities.state_id=states.id "
              "ORDER BY cities.id")
    a = c.fetchall()
    for row in a:
        print("{}".format(row))

    c.close()
    db.close()
