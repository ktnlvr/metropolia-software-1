from flask import Flask

from math import floor, sqrt

app = Flask(__name__)

def is_prime(n):
    return not any(n % i == 0 for i in range(2, n))

assert not is_prime(9999998)
assert is_prime(47)
assert not is_prime(1337)

@app.route('/prime_number/<n>')
def prime(n):
    n = int(n)
    return {'Number': n, 'isPrime': is_prime(n)}

app.run()
