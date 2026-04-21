# simple flask app - hello world
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define the route for the home page
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

# Run the app if this file is executed directly
if __name__ == "__main__":
    app.run()

