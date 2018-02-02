import numpy as np
import face_recognition
import cv2

imagePath = "images/Photo on 02-02-2018 at 18.38.jpg"

def test_face_recognition():
    print("Testing face_recognition module")

    image = face_recognition \
        .load_image_file(imagePath)

    face_landmarks_list = face_recognition.face_landmarks(image)

    print(len(face_landmarks_list))
    print("Can classify on :")
    print(face_landmarks_list[0].keys())

    print("For the right eye, the given data is:")
    print(face_landmarks_list[0].get('right_eye'))


def test_opencv():
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    img = cv2.imread('sachin.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    print("Testing opencv")
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier('openCVCascades/haarcascade_frontalface_default.xml')

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )






# test_face_recognition()
test_opencv()



# Notes:
#
# face_recognition easily installed using pip3 install face_recognition
#
# cv2 installed using pip3 install opencv-python
# but may rely on having an opencv installation already




