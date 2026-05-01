import os
from flask import Flask
from supabase import create_client, Client

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return f"Hello {name} from a GCP Microservice done by Rasik Shakya!"

@app.route("/count")
def count():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    supabase: Client = create_client(url, key)
    response = supabase.table("students").select("*", count="exact").execute()
    return f"Number of records in students table: {response.count}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host="0.0.0.0", port=port)
EOF
