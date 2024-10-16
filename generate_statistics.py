import requests
import csv
from flask import Flask

app = Flask(__name__)

@app.route('/statistics', methods=['GET'])
def generate_statistics():
    response = requests.get('http://calculate_scores:5002/scores')
    results = response.json()
    with open('statistics.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'total_score', 'max_diff'])
        writer.writeheader()
        writer.writerows(results)
    return "Statistics generated successfully"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
