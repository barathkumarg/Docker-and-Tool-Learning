# Flask app with Redis integration
from flask import Flask
import redis

# Create an instance of the Flask class
app = Flask(__name__)

# Connect to Redis
redis_client = redis.Redis(host='redis', port=6379, db=0)

# Define the route for the home page
@app.route("/")
def hello_world():
    # Increment counter in Redis
    counter = redis_client.incr('counter')
    return f"<h1>Hello, World!</h1><p>Page visits: {counter}</p>"

@app.route("/health")
def health_check():
    return {"status": "ok"}, 200

# Run the app if this file is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
