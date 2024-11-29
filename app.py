from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = "62c9a1eccaf9d4d047ba96108afac25e"  # Replace with your API key
FOOTBALL_URL = "https://v3.football.api-sports.io/fixtures"
BASKETBALL_URL = "https://v1.basketball.api-sports.io/games"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/secret.html')
def secret():
    return render_template('secret.html')

@app.route('/show_sport_info', methods=['POST'])
def show_sport_info():
    sport = request.form['sport']
    if sport.lower() == "football":
        headers = {"x-apisports-key": API_KEY}
        params = {"date": "2024-11-28"}  # Adjust date as needed
        response = requests.get(FOOTBALL_URL, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            fixtures = data.get('response', [])
            if fixtures:
                return render_template('football.html', fixtures=fixtures)
            else:
                return "No fixtures available for the specified date."

        else:
            return f"Error retrieving data from the API: {response.text}"

    elif sport.lower() == "basketball":
        headers = {"x-apisports-key": API_KEY}
        params = {"date": "2024-11-28"}  # Adjust date as needed
        response = requests.get(BASKETBALL_URL, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            games = data.get('response', [])
            if games:
                return render_template('basketball.html', games=games)
            else:
                return "No games available for the specified date."

        else:
            return f"Error from API: {data.get('errors', 'Unknown error')}"
    
    else:
        return "Invalid input. Please type 'football' or 'basketball' to get sports information."

if __name__ == '__main__':
    app.run(debug=True)
