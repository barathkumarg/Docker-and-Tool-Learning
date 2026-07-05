from flask import Flask, request 
import redis

app = Flask(__name__)

# redis connection
# redis-app 'name convention' for bridge network
# 127.0.0.1 for the host network
connect = redis.Redis(host="redis-app", port=6379, db=0)



# Create a route with basic html to get a key-value and post a key value from the redis
@app.route("/get", methods=["GET"])
def get_value():
    """
    Get the value of a key from Redis and display it in HTML format.
    """
    key = request.args.get("key")
    value = connect.get(key)
    return f"<h1>Value for key '{key}': {value}</h1>"

@app.route("/set", methods=["POST", "GET"])
def set_value():
    """
    Set the value of a key in Redis and display it in HTML format.
    """
    if request.method == "POST":
        key = request.form.get("key")
        value = request.form.get("value")
    else:
        # render the html form for GET request
        return '''
        <form method="post">
            <label for="key">Key:</label>
            <input type="text" id="key" name="key"><br><br>
            <label for="value">Value:</label>
            <input type="text" id="value" name="value"><br><br>
            <input type="submit" value="Set Value">
        </form>
        '''

    connect.set(key, value)
    return f"<h1>Value set for key '{key}': {value}</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)