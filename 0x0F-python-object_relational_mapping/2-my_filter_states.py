#!/usr/bin/python3
"""akes in an argument and displays all
 values in the states table of hbtn_0e_0_usa
  where name matches the argument."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    my_name = argv[1]
    my_pass = argv[2]
    my_db = argv[3]
    my_state = argv[4]
    db = MySQLdb.connect(passwd=my_pass, db=my_db,
                         user=my_name,
                         host="localhost", port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE states.name = %s"
              "ORDER BY states.id", (my_state,))
    a = c.fetchall()
    for row in a:
        print("{}".format(row))

    c.close()
    db.close()
