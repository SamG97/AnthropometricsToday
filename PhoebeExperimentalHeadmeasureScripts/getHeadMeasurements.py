# My suggested supported functions to get head measurements
import face_recognition
import numpy

cmPerPixel = 0.001

def getOcularWidth(imagepath):

    image = face_recognition \
        .load_image_file(imagepath)

    face_landmarks_list = face_recognition.face_landmarks(image)
    if len(face_landmarks_list) == 0:
        #No face detected
        #TODO: discuss what to do here
        return numpy.random.normal(10, 4)

    ocularWidthOfAllFacesPresent = []

    for face in face_landmarks_list:
        right_eye_points = face.get('right_eye')
        left_eye_points = face.get('left_eye')

        left_avg = get_average_xval(left_eye_points)
        right_avg = get_average_xval(right_eye_points)

        ocularWidthOfAllFacesPresent += [(right_avg - left_avg)*cmPerPixel]

    return max(ocularWidthOfAllFacesPresent)


def get_average_xval(points):
    averagex = 0.0
    for (x, y) in points:
        averagex += x
    averagex = averagex / len(points)
    return averagex


def getFaceWidth(imagepath):
    return 20

def getHeadLength(imagepath):
    #perform thresholding
    return 20


print(getOcularWidth("images/phoebe_face_glasses.jpg"))