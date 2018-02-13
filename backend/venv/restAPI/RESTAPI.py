from flask import Flask, request, make_response
from flask_jsonpify import jsonify

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/student/<int:student_id>', methods=['GET'])
def get_Student(student_id):
    #todo: hook up database so that it actually returns correct jason object
    return jsonify({'id': student_id})

def nearestNeigbour(image):
    return jsonify({'id': 100})

@app.route('/image_to_student', methods=['POST'])
def getNearestStudent(image):
    #todo: given the image calculate the nearest neighbour and return that students json
    return nearestNeigbour(request)

if __name__ == '__main__':
    app.run(port=5002)