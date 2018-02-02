import numpy as np
import face_recognition
import cv2

phoebe_face = "images/phoebe_face_noglasses.jpg"
phoebe_profile = "images/phoebe_profile_right.jpg"
rando_profile = "images/rando_profileface_left.jpg"

def test_face_recognition():
    print("Testing face_recognition module")

    image = face_recognition \
        .load_image_file(phoebe_face)

    face_landmarks_list = face_recognition.face_landmarks(image)

    print(len(face_landmarks_list))
    print("Can classify on :")
    print(face_landmarks_list[0].keys())

    print("For the right eye, the given data is:")
    print(face_landmarks_list[0].get('right_eye'))


def test_opencv_faces():

    face_cascade = cv2.CascadeClassifier('openCVCascades/haarcascade_frontalface_default.xml')

    img = cv2.imread(phoebe_face)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(faces[0])
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imwrite('output/opencv_for_facewidth.jpg', img)

def test_opencv_profiles():
    profile_cascade = cv2.CascadeClassifier(
        'openCVCascades/haarcascade_profileface.xml')

    img = cv2.imread(rando_profile)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    profiles = profile_cascade.detectMultiScale(gray, 1.3, 5)
    print(profiles[0])
    for (x, y, w, h) in profiles:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imwrite('output/opencv_for_profiles.jpg', img)


# test_face_recognition()
# test_opencv_faces()
test_opencv_profiles()

# Notes:
#
# face_recognition easily installed using pip3 install face_recognition
#
# cv2 installed using pip3 install opencv-python
# but may rely on having an opencv installation already
# and openCV is genreally a massive pain in the ass




