import face_recognition
import cv2
from PIL import Image, ImageDraw

all_faces = ["images/phoebe_face_noglasses.jpg",
             "images/phoebe_face_glasses.jpg",
             "images/random_dude_face.jpg",
             "images/face_with_hair.jpeg"]

all_profiles = ["images/phoebe_profile_right.jpg",
                "images/phoebe_profile_left.jpg",
                "images/rando_profileface_left.jpg",
                "images/rando_profileface_right.jpg"]

base_location = "images/"


def test_face_recognition(imagepath):
    print("Testing face_recognition package")

    image = face_recognition \
        .load_image_file(imagepath)

    face_landmarks_list = face_recognition.face_landmarks(image)
    if len(face_landmarks_list) == 0:
        print("No face detected")
        return

    print(str(len(face_landmarks_list)) + ' faces detected')

    im = Image.open(imagepath)
    draw = ImageDraw.Draw(im)

    for face in face_landmarks_list:
        for landmark in face:
            points = face.get(landmark)
            for coord in points:
                draw.point(coord)
    del draw
    location = 'output/face_recognition_package/' + imagepath[
                                                    len(base_location):]
    im.save(location, "JPEG")


def test_opencv_faces(imagepath):
    face_cascade = cv2.CascadeClassifier(
        'openCVCascades/haarcascade_frontalface_default.xml')

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

    location = 'output/opencv_for_face_width/' + imagepath[len(base_location):]
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


for face in all_faces:
    test_face_recognition(face)

for face in all_faces:
    test_opencv_faces(face)
    test_opencv_profiles(face)

for profile in all_profiles:
    test_opencv_profiles(profile)

# Notes:
#
# face_recognition_package easily installed
# using pip3 install face_recognition_package
#
# cv2 installed using pip3 install opencv-python
# but openCV is generally a massive pain in the ass
