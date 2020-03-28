#!/usr/bin/python3
""" Get all states """

import MySQLdb
import sys

if __name__ == "__main__":
    my_name = sys.argv[1]
    my_pass = sys.argv[2]
    my_db = sys.argv[3]
    db = MySQLdb.connect(passwd=my_pass, db=my_db,
                         user=my_name,
                         host="localhost", port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM hbtn_0e_0_usa.states ORDER BY states.id")
    a = c.fetchall()
    for row in a:
        print(row)

    c.close()
    db.close()
