import requests

if __name__ == '__main__':
    response = requests.get('https://api.chucknorris.io/jokes/random')
    print(response.json()['value'])
