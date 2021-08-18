from flask import Flask

import socket

app = Flask(__name__)

@app.route("/")
def hello():
    return '{hostname: "' + socket.gethostname() + '", version: "V3", language: "python3"}', 200, {'content-type': 'application/json'}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)