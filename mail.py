from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

UNIVERSE_ID = 7943671731  # Замени на свой UniverseId

@app.route("/visits")
def visits():
    url = f"https://games.roblox.com/v1/games?universeIds={UNIVERSE_ID}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        visits = data['data'][0]['visits']
        return jsonify({"visits": visits})
    return jsonify({"visits": 0})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
