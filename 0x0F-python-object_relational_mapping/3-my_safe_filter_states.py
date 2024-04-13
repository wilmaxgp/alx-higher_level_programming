#!/usr/bin/python3
"""
Lists all states where the name matches
the argument passed (safe from MySQL injection)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                   (search,))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
