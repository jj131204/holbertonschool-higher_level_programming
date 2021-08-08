#!/usr/bin/python3

""""""
if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
