from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self, student_id):
        #todo: hook up database so that it actually returns correct jason object
        return {'id': student_id}

def nearestNeigbour(image):
    return {'id': 100};

class Image_to_Student(Resource):
    def get(self, image):
        #todo: given the image calculate the nearest neighbour and return that students json
        return nearestNeigbour(image)

api.add_resource(Student, '/student/<student_id>')
api.add_resource(Image_to_Student, '/image_to_student/<image>')

if __name__ == '__main__':
    app.run(port=5002)