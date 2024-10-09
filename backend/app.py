from flask import Flask, request, jsonify
from tester import test_repository
import os

app = Flask(__name__)

@app.route('/test_repo', methods=['POST'])
def test_repo():
    data = request.json
    repo_url = data['repo_url']
    result = test_repository(repo_url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
