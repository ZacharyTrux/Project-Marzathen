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

@app.route('/getStandings', methods=['GET'])
def get_standings():
    team = request.args.get('team')  # Get the team from the URL parameters
    sport = request.args.get('sport')  # Get the sport from the URL parameters

    # Validate inputs
    #if not team or not sport:
        #return jsonify({"error": "Missing 'team' or 'sport' parameter"}), 400
    
    # Example: Fetch data from an API based on sport and team
    # This assumes you have an external API that gives standings data

    if sport.lower() == 'football':
        # Assuming the team name needs to be formatted or replaced
        team = team.replace("-", " ").title()
        url = f"https://site.api.espn.com/apis/v2/sports/football/nfl/standings?season=2024"
        try:
            response = requests.get(url)
            standings_data = response.json()

            # Logic to filter the standings by team can be added here
            team_data = next((team_info for team_info in standings_data['sports'][0]['leagues'][0]['standings']['entries'] if team_info['team']['displayName'].lower() == team.lower()), None)

            if team_data:
                return jsonify({
                    "team": {
                        "name": team_data['team']['displayName'],
                        "abbreviation": team_data['team']['abbreviation'],
                        "location": team_data['team']['location'],
                        "record": {
                        "wins": team_data['record']['wins'],
                        "losses": team_data['record']['losses'],
                        "winPercentage": team_data['record']['winPercentage']
                    },
                    "position": team_data['position']
                    }
                })
            else:
                return jsonify({"error": f"Team '{team}' not found in standings."}), 404

        except requests.exceptions.RequestException as e:
            return jsonify({"error": "Error fetching data from ESPN API", "details": str(e)}), 500

    else:
        return jsonify({"error": "Sport not supported."}), 400


if __name__ == '__main__':
    app.run(debug=True)
