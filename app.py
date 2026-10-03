from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>KubeBattle v2 </title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f7fb;
                text-align: center;
                padding: 80px;
            }}

            .card {{
                max-width: 650px;
                margin: auto;
                background: white;
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            }}

            h1 {{
                color: #1f2937;
            }}

            .status {{
                display: inline-block;
                padding: 10px 18px;
                border-radius: 20px;
                background: #dcfce7;
                color: #166534;
                font-weight: bold;
            }}

            .pod {{
                margin-top: 25px;
                padding: 15px;
                background: #f1f5f9;
                border-radius: 10px;
                font-family: monospace;
            }}
        </style>
    </head>

    <body>
        <div class="card">
            <h1>⚔️ KubeBattle</h1>

            <p class="status">Kubernetes Pod Healthy</p>

            <h2>Failure & Recovery Lab</h2>

            <p>
                This application is running inside a Kubernetes Pod.
            </p>

            <div class="pod">
                Pod: {hostname}
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "pod": socket.gethostname()
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
