from functools import lru_cache
from db import get_connection

@lru_cache(maxsize=256)
def fetch_location(icao: str) -> tuple[str, str] | None:
    # SQL INJECTION LETS GO
    query = f"select municipality,name from airport where ident = '{icao}'"
    cursor = get_connection().cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    if cursor.rowcount == 0:
        return None
    elif cursor.rowcount > 1:
        raise Exception("ICAO code not unique, more than one primary key, the database is cursed")
    else:
        return result[0]

if __name__ == "__main__":
    icao = input("Enter ICAO: ").strip().upper()
    if result := fetch_location(icao):
        location, name = result
        print(location)
        print(name)
    else:
        print("Failed to find airport `{icao}`.")
