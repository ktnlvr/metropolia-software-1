from flask import Flask
import csv

app = Flask(__name__)

airports = {}
with open('../airports.csv', mode='r', encoding='utf8') as f:
    reader = csv.reader(f)
    for row in list(reader)[1:]:
        # this is too funny
        _, icao, _, name, *_, location = row[:-7]
        airports[icao] = name, location


@app.route('/airport/<icao>')
def index(icao: str):
    # sql injection yippie
    if icao not in airports:
        return {"err": "error, sowwy, this airport doesn't exist :c"}
    name, location = airports[icao]
    return {'ICAO': icao, 'Name': name, 'Location': location}

app.run()