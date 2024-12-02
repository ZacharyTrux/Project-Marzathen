from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/developerInfo.html')
def secret():
    return render_template('developerInfo.html')

team_codes = {
    "arizona-cardinals": "1",
    "atlanta-falcons": "2",
    "baltimore-ravens": "3",
    "buffalo-bills": "4",
    "carolina-panthers": "5",
    "chicago-bears": "6",
    "cincinnati-bengals": "7",
    "cleveland-browns": "8",
    "dallas-cowboys": "9",
    "denver-broncos": "10",
    # Add all other teams here...
}

@app.route('/getStandings', methods=['GET'])
def get_standings():
    team = request.args.get('team')
    sport = request.args.get('sport')

    if not team or not sport:
        return jsonify({"error": "Missing team or sport parameters"}), 400

    try:
        # URL for the ESPN API
        url = f"https://site.api.espn.com/apis/site/v2/sports/{sport.lower()}/nfl/{team}/roster"
        response = requests.get(url)

        if response.status_code != 200:
            return jsonify({"error": f"Failed to fetch data from ESPN API: {response.status_code}"}), 500

        # Return the response as JSON
        data = response.json()
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
