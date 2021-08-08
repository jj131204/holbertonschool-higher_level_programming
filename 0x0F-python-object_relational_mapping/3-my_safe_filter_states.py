#!/usr/bin/python3
"""takes in an argument and displays all values in the states"""

if __name__ == '__main__':
    """main"""

    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name=$s\
                ORDER BY states.id ASC", (argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
