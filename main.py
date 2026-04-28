import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return f"Hello {name} from a GCP Microservice!"

if __name__ == "__main__":
    # Cloud Run provides a PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host="0.0.0.0", port=port)
