from flask import Flask, render_template


app = Flask(__name__)


# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for the secret page
@app.route('/secret')
def secret():
    return render_template('secret.html')

if __name__ == '__main__':
    app.run()  # No need to specify debug=True here, it's set in the config
