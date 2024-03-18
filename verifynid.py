from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/verify-nid', methods=['GET'])
def verify_nid():
    nid = request.args.get('nid')
    dob = request.args.get('dob')
    
    if not nid or not dob:
        return jsonify({'error': 'NID and DOB parameters are required'}), 400
    
    url = 'https://apps.ecs.gov.bd/api/v1/real-verify-nid/'
    headers = {
        'User-Agent': 'Dart/3.1 (dart:io)',
        'Accept-Encoding': 'gzip',
        'Content-Type': 'application/json'
    }
    data = {
        'dob': dob,
        'searchValue': nid
    }
    response = requests.post(url, headers=headers, json=data)
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
