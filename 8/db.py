from mysql.connector import connect

_connection = None

def get_connection():
    global _connection
    if _connection is None:
        _connection = connect(host="localhost", port=3306, database="flight_game", user="admin", autocommit=True)
    return _connection
