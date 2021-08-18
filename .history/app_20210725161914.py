from flask import Flask

import socket

app = Flask(__name__)

@app.route("/")
def hello():
    response = Flask.make_response('{hostname: "' + socket.gethostname() + '", version: "V2", language: "python3"}')
    response.headers['content-type'] = 'application/octet-stream'
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)