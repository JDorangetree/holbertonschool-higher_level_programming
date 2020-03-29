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
    txtSQL = ("SELECT cities.name FROM cities INNER JOIN states "
              "ON cities.state_id=states.id WHERE states.name LIKE BINARY %s")
    c.execute(txtSQL, (my_state,))
    a = c.fetchall()
    to_print = []
    for row in a:
        to_print.append(row[0])

    print(", ".join(to_print))
    c.close()
    db.close()
