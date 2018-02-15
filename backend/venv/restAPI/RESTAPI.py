from flask import Flask, request, make_response, abort
from flask_jsonpify import jsonify
from restAPI.Dummy_process import getPersonDataById, getClosestRecord, ReturnObjects

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

def nearestNeigbour(studentList):
    students = [{studentList.get()[j][i][0]: studentList.get()[j][i][1] for i in range(len(studentList.get()[j]))}
                for j in range(len(studentList.get()))]
    dist = [students[i]['id'] for i in range(len(students))]
    min = dist[0]
    index = 0
    for i in range(len(dist)):
        if dist[i] < min:
            min = dist[i]
            index = i

    return jsonify({'id':students[index]['id'], 'fromwhere':'new'})

@app.route('/image_to_student', methods=['POST'])
def getNearestStudent():
    #dimensions = proccessImage(request.json['body']['image']['uri'])
    dimensions = [189, 145, 137]
    studentList = getClosestRecord(dimensions[0], dimensions[1], dimensions[2], 19, 136)
    return nearestNeigbour(studentList)

if __name__ == '__main__':
    app.run(port=5002)