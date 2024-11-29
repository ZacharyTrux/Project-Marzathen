from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "62c9a1eccaf9d4d047ba96108afac25e"  # Replace with your API key
BASE_URL = "https://v3.football.api-sports.io/fixtures"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/secret.html')
def secret():
    return render_template('secret.html')


@app.route('/show_football_info', methods=['POST'])
def show_football_info():
    sport = request.form['sport']
    if sport.lower() == "football":
        # API request to get today's fixtures
        headers = {"x-apisports-key": API_KEY}
        params = {"date": "2024-11-28"}  # Adjust date as per your plan
        response = requests.get(BASE_URL, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            fixtures = data.get('response', [])
            if fixtures:
                # Display basic information about the fixtures
                return render_template('football.html', fixtures=fixtures)
            else:
                return "No fixtures available for the specified date."
        else:
            return f"Error retrieving data from the API: {response.text}"
    else:
        return "Invalid input. Please type 'football' to get football information."

if __name__ == '__main__':
    app.run(debug=True)
