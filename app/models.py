import cx_Oracle

CONN_INFO = {
    "host":    "192.168.1.12",
    "port":    "1521",
    "user":    "system",
    "pswd":    "oracle",
    "service": "orcl"
}

CONN_STR = "{user}/{pswd}@{host}:{port}/{service}".format(**CONN_INFO)

users = [
    {
        "name": "User1",
        "age":  33,
        "city": "Berlin"
    },
    {
        "name": "User2",
        "age": 22,
        "city": "Warsaw"
    },
    {
        "name": "User3",
        "age": 11,
        "city": "Tokyo"
    },
]


class Oracle:
    def __init__(self):
        print(CONN_STR)
        try:
            self.conn = cx_Oracle.connect(CONN_STR)
            print(self.conn.version)
        except:
            print("No database connection")
        #self.conn.close()  # na razie - do wylaczenia

    def query(self, q, params={}):
        try:
            cursor = self.conn.cursor()
            result = cursor.execute(q, params).fetchall()
            cursor.close()
        except AttributeError:
            result = None
        finally:
            return result
