from flask import Flask, request, make_response, abort
from flask_jsonpify import jsonify
from restAPI.Dummy_process import getPersonDataById, getClosestRecord

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 400)

@app.route('/student/<string:fromwhere>/<int:student_id>', methods=['GET'])
def get_Student(fromwhere,student_id):
    data = getPersonDataById(student_id,fromwhere) #problem with out of index ids
    if (data == None):
        abort(400)
    student = {data[i][0] : data[i][1] for i in range(len(data))}
    return jsonify(student)

def nearestNeigbour(image):
    return jsonify({'id': 100})

@app.route('/image_to_student', methods=['POST'])
def getNearestStudent():
    dimensions = proccessImage(request.json['body']['image']['uri'])
    studentList = getClosestRecord(dimensions[0], dimensions[1], dimensions[2])
    return nearestNeigbour(studentList)

if __name__ == '__main__':
    app.run(port=5002)