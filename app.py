from flask import Flask, render_template, jsonify, request
from selenium_script import main

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    data = request.get_json()
    TWITTER_USERNAME = data.get('username')
    TWITTER_PASSWORD = data.get('password')

    # Validate the inputs (optional)
    if not TWITTER_USERNAME or not TWITTER_PASSWORD:
        return jsonify({"error": "Username and password are required."}), 400
    
    result = main(TWITTER_USERNAME, TWITTER_PASSWORD)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
