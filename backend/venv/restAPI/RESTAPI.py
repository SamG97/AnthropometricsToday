from flask import Flask, request, make_response
from flask_jsonpify import jsonify
from restAPI.Dummy_process import getPersonDataById, getClosestRecord

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/student/<int:student_id>', methods=['GET'])
def get_Student(student_id):
    return jsonify(getPersonDataById(student_id))

def nearestNeigbour(image):
    return jsonify({'id': 100})

@app.route('/image_to_student', methods=['POST'])
def getNearestStudent():
    dimensions = proccessImage(request.json['body']['image']['uri'])
    studentList = getClosestRecord(dimensions[0], dimensions[1], dimensions[2])
    return nearestNeigbour(studentList)

if __name__ == '__main__':
    app.run(port=5002)