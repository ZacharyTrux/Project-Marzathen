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
    
    response = requests.get(url)
    data = response.json()
        
        # Search for the specific team in the standings data
    standings = data['children'][0]['standings']['entries']
    for entry in standings:
        team_name = entry['team']['name']
            
        if team_name.lower() == team.lower():
                
            stats = entry["stats"]
            standings_data = {
                    "gamesPlayed": next(s["value"] for s in stats if s["name"] == "gamesPlayed"),
                    "wins": next(s["value"] for s in stats if s["name"] == "wins"),
                    "ties": next((s["value"] for s in stats if s["name"] == "ties"), 0),  # Handle if ties are missing
                    "losses": next(s["value"] for s in stats if s["name"] == "losses"),
                    "pointsFor": next(s["value"] for s in stats if s["name"] == "pointsFor"),
                    "pointsAgainst": next(s["value"] for s in stats if s["name"] == "pointsAgainst"),
                    "pointDifferential": next(s["value"] for s in stats if s["name"] == "pointDifferential"),
                    "points": next(s["value"] for s in stats if s["name"] == "points"),
                }
    return jsonify(standings_data)
            
        

if __name__ == '__main__':
    app.run(debug=True)
