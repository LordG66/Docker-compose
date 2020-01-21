from flask import *
from datetime import datetime

app = Flask(__name__)
@app.route('/')
def main():
    time = datetime.now()
    with open("usage.log", "a+") as file:
        file.write("read at {}\n".format(time))
    return render_template('index.html', text="Time is {}".format(time))
@app.route('/usage.log')
def show():
    with open("usage.log", "r") as file:
        log = file.read()
    return render_template('index.html', text=log)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
