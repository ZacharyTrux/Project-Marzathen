from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/developerInfo.html')
def secret():
    return render_template('developerInfo.html')

@app.route('/get_standings', methods=['GET'])
def get_standings():
    team = request.args.get('team')
    sport = request.args.get('sport')

    # Make API request to ESPN standings endpoint
    url = f"https://site.api.espn.com/apis/site/v2/sports/{sport}/{sport}/standings"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Search for the specific team in the standings data
        team_data = None
        for conference in data['children']:
            for team_info in conference['standings']['entries']:
                if team_info['team']['displayName'].lower() == team.lower():
                    team_data = team_info
                    break
            if team_data:
                break
        
        if team_data:
            return jsonify(team_data)
        else:
            return jsonify({"error": "Team not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
