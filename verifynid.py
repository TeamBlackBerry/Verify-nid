from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/verify-nid', methods=['POST'])
def verify_nid():
    url = 'https://apps.ecs.gov.bd/api/v1/real-verify-nid/'
    headers = {
        'User-Agent': 'Dart/3.1 (dart:io)',
        'Accept-Encoding': 'gzip',
        'Content-Type': 'application/json'
    }
    data = request.json
    response = requests.post(url, headers=headers, json=data)
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
