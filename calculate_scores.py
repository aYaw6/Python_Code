import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/scores', methods=['GET'])
def calculate_scores():
    response = requests.get('http://grade_service:5001/grades')
    grades = response.json()
    results = []
    for student in grades:
        scores = [int(student[subject]) for subject in student if subject != 'Name']
        total_score = sum(scores)
        max_diff = max(scores) - min(scores)
        results.append({'name': student['Name'], 'total_score': total_score, 'max_diff': max_diff})
    return jsonify(results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
