# create a sample fat api application , endpoint /health and it returns the healthy on response
# create a enpoint where it checks the given number is prime endpoint /isprime?number=n
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def read_health():
    return {"status": "healthy"}


@app.get("/isprime")
def check_prime(number: int):
    if number < 2:
        return {"number": number, "is_prime": False}
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return {"number": number, "is_prime": False}
    return {"number": number, "is_prime": True}