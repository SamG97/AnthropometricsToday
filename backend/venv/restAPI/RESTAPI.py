from flask import Flask, request, make_response, abort
from flask_jsonpify import jsonify
from restAPI.Dummy_process import getPersonDataById, getClosestRecordSet, ReturnObjects
from restAPI.NearestNeigbour import calcNearestNeigbour
from restAPI.headMeasure import proccessImage

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
    students = [{studentList.get()[j][i][0]: studentList.getall()[j][i][1] for i in range(len(studentList.getall()[j]))}
                for j in range(len(studentList.getall()))]
    dists = [students[i]['id'] for i in range(len(students))]
    return jsonify({'id':students[calcNearestNeigbour(dists)]['id'], 'fromwhere':'new'})

@app.route('/image_to_student', methods=['POST'])
def getNearestStudent():
    dimensions = proccessImage(request.json['body']['image1']['uri'], request.json['body']['image2']['uri'])
    #dimensions = [189, 145, 137]
    studentList = getClosestRecordSet(dimensions[0], dimensions[1], dimensions[2], 19, 136)
    return nearestNeigbour(studentList)

if __name__ == '__main__':
    app.run(port=5002)

#problems:
#need a field in database to state whitch card type the student is from
#need the database names to be consistent and that the units in the data base are consistent
#need to catch excepions in database code and then return a None if index out of range
#need to hook up the image processing unit to the api to combine backend
#need to add all files and packeages to the backend venv on git and then only use that version
#need to talk about intefaces between the backend units, arguments and retuen values and function names
#need to then perform integration testing