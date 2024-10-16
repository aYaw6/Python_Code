import csv
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/grades', methods=['GET'])
def read_grades():
    with open('GradeTable.csv', mode='r') as file:
        reader = csv.DictReader(file)
        grades = [row for row in reader]
    return jsonify(grades)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

