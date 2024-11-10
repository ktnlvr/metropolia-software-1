import requests

key = "b962268534daa76de918e28bd5102834"

if __name__ == '__main__':
    city = input("Enter municipality: ")
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}")
    data = response.json()
    print(round(data["main"]["temp"]-273.15, 1))
    for weather in data["weather"]:
        print(weather['description'])
