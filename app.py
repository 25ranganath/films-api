from flask import Flask

# add mysql dependency and make a flask-mysql template project
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Mom! and Dad!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

