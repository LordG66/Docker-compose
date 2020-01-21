from flask import *
import requests

app = Flask(__name__)
@app.route('/')
def main():
    log = requests.get('http://timeservice:5001/usage.log')
    return render_template('index.html', text=log.text.strip('<pre></'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
