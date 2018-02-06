import MySQLdb

mysql = MySQLdb.connect(host="localhost", db="flask_test", user="root")


def post_data_to_mysql(content):
    # content format: (tag, data)
    with mysql as db:
        # This is for fun, and we all know doing this is bad, but that's not the point
        quert_string = "INSERT INTO flask_data VALUES(%s, %s)"
        cur.execute(query_string, content)
        cur.commit()
        return 


def get_data_from_mysql():
    data = []
    with mysql as db:
        cur = db.cursor()
        query_string = "SELECT tag, data FROM flask_data"
        cur.execute(query_string)
        for row in cur.fetchall():
            data.append(row)
    return data



