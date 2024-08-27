from math import sqrt
from geopy import distance

from db import get_connection

def get_coords(icao: str) -> None | tuple[float, float, float]:
    query = f"select latitude_deg,longitude_deg,elevation_ft from airport where ident = '{icao}'"
    cursor = get_connection().cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    if cursor.rowcount != 1:
        return None
    else:
        lat, long, elevation = result
        return lat, long, elevation * 0.0003048

if __name__ == '__main__':
    icao1 = input("Enter ICAO 1: ").strip().upper()
    icao2 = input("Enter ICAO 2: ").strip().upper()
    pos1 = get_coords(icao1)
    pos2 = get_coords(icao2)
    if pos1 is None:
        print(f"Couldn't find airport {icao1}")
    elif pos2 is None:
        print(f"Couldn't find airport {icao2}")
    lat1, lon1, alt1 = pos1
    lat2, lon2, alt2 = pos2
    dH = alt2 - alt1
    d2D = distance.geodesic((lat1, lon1), (lat2, lon2))
    d = sqrt(dH*dH + d2D*d2D)
