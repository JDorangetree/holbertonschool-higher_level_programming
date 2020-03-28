#!/usr/bin/python3
""" Get all states """

if __name__ == "__main__":

    import MySQLdb
    import sys

    my_name = sys.argv[1]
    my_pass = sys.argv[2]
    my_db = sys.argv[3]
    db = MySQLdb.connect(passwd=my_pass, db=my_db, user=my_name)
    c = db.cursor()
    c.execute("""SELECT * FROM hbtn_0e_0_usa.states ORDER BY id""")
    a = c.fetchall()
    for row in a:
        print("{}".format(row))
    # Close all cursors
    c.close()
    # Close all databases
    db.close()
