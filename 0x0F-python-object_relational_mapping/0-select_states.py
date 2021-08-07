#!/usr/bin/python3
"""test1"""
if __name__ == '__main__':
    """main"""

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], password=argv[2], db=argv[3])

    cursor = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
