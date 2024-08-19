airports = {
    "EFHK": "Helsinki-Vantaa Airport",
    "SJRG": "Rio Grande Airport",
    "EVRA": "Riga International Airport",
    "UGSB": "Alexander Kartveli Batumi International Airport",
}

if __name__ == '__main__':
    while True:
        print("`add` or `fetch`?")
        action = input(">> ").strip().lower()
        if action == "add":
            icao = input("ICAO: ").strip().upper()
            name = input("Name: ").strip()
            if icao in airports:
                print(f"WARN! Overriding an existing airport `{icao}` '{airports[icao]}'")
            airports[icao] = name
        elif action == "fetch":
            icao = input("ICAO: ").strip().upper()
            if icao in airports:
                print(f"      {airports[icao]}")
            else:
                print(f"WARN! No airport `{icao}` found")