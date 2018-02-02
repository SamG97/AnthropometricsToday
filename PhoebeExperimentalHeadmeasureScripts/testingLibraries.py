import numpy as np
import face_recognition
import cv2

all_faces = ["images/phoebe_face_noglasses.jpg",
              "images/phoebe_face_glasses.jpg"]

all_profiles = ["images/phoebe_profile_right.jpg",
                "images/phoebe_profile_left.jpg",
                "images/rando_profileface_left.jpg",
                "images/rando_profileface_right.jpg"]

base_location = "images/"

def test_face_recognition(imagepath):
    print("Testing face_recognition module")

    image = face_recognition \
        .load_image_file(imagepath)

    face_landmarks_list = face_recognition.face_landmarks(image)
    if (len(face_landmarks_list) == 0):
        print("No face detected")

    print("Face detected")

    print(len(face_landmarks_list))
    print("Can classify on :")
    print(face_landmarks_list[0].keys())

    print("For the right eye, the given data is:")
    print(face_landmarks_list[0].get('right_eye'))

def test_opencv_faces(imagepath):
    face_cascade = cv2.CascadeClassifier('openCVCascades/haarcascade_frontalface_default.xml')

    img = cv2.imread(imagepath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(faces)
    print(type(faces))
    if faces == ():
            print("No face detected")
            return
    print("Face detected")
    print(faces[0])
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    location = 'output/opencv_for_face_width/'+imagepath[len(base_location):]
    cv2.imwrite(location, img)

def test_opencv_profiles(imagepath):
    profile_cascade = cv2.CascadeClassifier(
        'openCVCascades/haarcascade_profileface.xml')

    img = cv2.imread(imagepath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    profiles = profile_cascade.detectMultiScale(gray, 1.3, 5)
    if profiles == ():
            print("No profiles detected")
            return
    print(profiles[0])
    for (x, y, w, h) in profiles:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    location = 'output/opencv_for_profiles/' + imagepath[len(base_location):]
    cv2.imwrite(location, img)


# test_face_recognition()
for face in all_faces:
    test_opencv_faces(face)

for profile in all_profiles:
    test_opencv_profiles(profile)

# Notes:
#
# face_recognition easily installed using pip3 install face_recognition
#
# cv2 installed using pip3 install opencv-python
# but may rely on having an opencv installation already
# and openCV is genreally a massive pain in the ass




