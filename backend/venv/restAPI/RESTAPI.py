from flask import Flask, request, make_response, abort
from flask_jsonpify import jsonify
from restAPI.DataBaseScript import getPersonDataById, getClosestRecordSet, ReturnObjects
from restAPI.NearestNeigbour import calcNearestNeigbour
#from restAPI.headMeasure import proccessImage

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 400)

@app.route('/student/<int:student_id>', methods=['GET'])
def get_Student(student_id):
    data = getPersonDataById(student_id)
    if (data == None):
        abort(400)
    student = {data[i][0] : data[i][1] for i in range(len(data))}
    return jsonify(student)

def processStudents(studentList):
    [{studentList.getall()[j][i][0]: studentList.getall()[j][i][1] for i in range(len(studentList.getall()[j]))}
     for j in range(len(studentList.getall()))]

def getDists(students):
   return [[students[i]['Face_iobreadth'], students[i]['Face_breadth'], students[i]['Head_length']] for i in
     range(len(students))]

def nearestNeigbour(studentList, node):
    students = processStudents()
    dists = getDists()
    index = calcNearestNeigbour(node, dists)
    return jsonify({'id':students[index]['id'],
                    'Face_iobreadth':node[0],
                    'Face_breadth':node[1],
                    'Head_length':node[2]})

#@app.route('/image_to_student', methods=['POST'])
#def getNearestStudent():
#    dimensions = proccessImage(request.json['body']['image1']['uri'], request.json['body']['image2']['uri'])
#    studentList = getClosestRecordSet(dimensions[0], dimensions[1], dimensions[2])
#    return nearestNeigbour(studentList, dimensions)

if __name__ == '__main__':
    app.run(port=5002)

