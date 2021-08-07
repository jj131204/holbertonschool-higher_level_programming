#!/usr/bin/python3
"""test1"""
if __name__ == "__main__":
    """main"""

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], password=sys.argv[2],  db=sys.argv[3])

    cursor = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
