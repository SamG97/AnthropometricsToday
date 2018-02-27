from flask import Flask, request, make_response, abort
from flask_jsonpify import jsonify
from restAPI.DataBaseScript import getPersonDataById, getClosestRecordSet, ReturnObjects
from restAPI.NearestNeigbour import calcNearestNeigbour
#from restAPI.headMeasure import proccessImage
from datetime import timedelta
from functools import update_wrapper
import base64

app = Flask(__name__)
lastID = [-1]

def crossdomain(origin=None, methods=None, headers=None, max_age=21600,
                attach_to_all=True, automatic_options=True):
    """Decorator function that allows crossdomain requests.
      Courtesy of
      https://blog.skyred.fi/articles/better-crossdomain-snippet-for-flask.html
    """
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, list):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, list):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        """ Determines which methods are allowed
        """
        if methods is not None:
            return methods

        options_resp = app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        """The decorator function
        """
        def wrapped_function(*args, **kwargs):
            """Caries out the actual cross domain code
            """
            if automatic_options and request.method == 'OPTIONS':
                resp = app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

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

def getLastIDIndex(students):
    i = 0
    while i < len(students) and students[i]['id'] != lastID[0]:
        i += 1
    return i

def nearestNeigbour(studentList, node):
    students = [{studentList.getall()[j][i][0]: studentList.getall()[j][i][1] for i in range(len(studentList.getall()[j]))}
                 for j in range(len(studentList.getall()))]
    if(len(students) > 1):
        i = getLastIDIndex(students)
        if (i < len(students)):
            students.remove(students[i])
    dists = [[students[i]['Face_iobreadth'], students[i]['Face_breadth'], students[i]['Head_length']] for i in
              range(len(students))]
    index = calcNearestNeigbour(node, dists)
    lastID[0] = students[index]['id']
    return jsonify({'id': lastID[0],
                    'Face_iobreadth':node[0],
                    'Face_breadth':node[1],
                    'Head_length':node[2]})

def base64ToFile(fileName, img_data):
    with open("imageToSave.png", "wb") as fh:
        fh.write(base64.decodebytes(img_data))

@app.route('/image_to_student', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def getNearestStudent():
#   sideShot = request.json['body']['user_photo1']['uri'] #may also need to remove the header from this
#   frontShot = request.json['body']['user_photo1']['uri']
#   base64ToFile("sideShot.png", sideShot)
#   base64ToFile("frontShot.png", frontShot)
#   dimensions = proccessImage("sideShot.png", "frontShot.png")
    dimensions = [100,100,100]
    studentList = getClosestRecordSet(dimensions[0], dimensions[1], dimensions[2])
    return nearestNeigbour(studentList, dimensions)

if __name__ == '__main__':
    app.run(port=5002)

