from db import get_connection
from itertools import groupby

if __name__ == '__main__':
    area_code = input("Enter an area code: ").strip().upper()

    query = f"select type,name from airport where iso_country = '{area_code}' order by type";
    cursor = get_connection().cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    for t, airports in groupby(result, lambda x: x[0]):
        airports = list(airports)
        type_name = t.replace('_', ' ').title()
        print(f"--- {len(airports)} airports of type {type_name} ---")
        for _, airport in airports:
            print(airport)