from flask import Flask
from routes.movies import movies_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(movies_bp)

@app.route('/')
def index():
    return "Movie API is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
