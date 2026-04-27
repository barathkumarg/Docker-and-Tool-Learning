from flask import Flask
from redis import Redis

app = Flask(__name__)
# "redis" is the hostname defined in docker-compose.yml
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    # Increment the counter in Redis
    count = redis.incr('hits')
    
    # Simple HTML UI
    return f"""
    <div style="text-align: center; margin-top: 50px; font-family: sans-serif;">
        <h1>🚀 Flask + Redis Counter</h1>
        <p style="font-size: 24px;">This page has been viewed <b>{count}</b> times.</p>
        <button onclick="location.reload()">Refresh to Count</button>
    </div>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)