# Phoebe's suggested functions to get head measurements

import face_recognition
import numpy
from skimage import data, color
from skimage.filters import threshold_mean

cmPerPixel = 0.0458


def getOcularWidth(image_path):
    image = face_recognition \
        .load_image_file(image_path)

    face_landmarks_list = face_recognition.face_landmarks(image)

    if len(face_landmarks_list) == 0:
        # No face detected
        # TODO: discuss what to do here
        return numpy.random.normal(6, 1)

    ocularWidthOfAllFacesPresent = []

    for face in face_landmarks_list:
        right_eye_points = face.get('right_eye')
        left_eye_points = face.get('left_eye')

        left_avg = get_average_x(left_eye_points)
        right_avg = get_average_x(right_eye_points)

        ocularWidthOfAllFacesPresent += [(right_avg - left_avg) * cmPerPixel]

    return max(ocularWidthOfAllFacesPresent)


def getFaceWidth(image_path):
    image = face_recognition \
        .load_image_file(image_path)

    face_landmarks_list = face_recognition.face_landmarks(image)

    if len(face_landmarks_list) == 0:
        # No face detected
        # TODO: discuss what to do here
        return numpy.random.normal(15, 2)

    widthOfAllFacesPresent = []

    for face in face_landmarks_list:
        points = face.get('chin')
        x_points = []
        for (x, y) in points:
            x_points += [x]
        widthOfAllFacesPresent += [(max(x_points) - min(x_points)) * cmPerPixel]

    return max(widthOfAllFacesPresent)


def getHeadLength(image_path):
    binary = getThresholdImage(image_path)
    mid_point = len(binary) // 2
    row = binary[mid_point]

    most_consecutive_falses = 0
    current_consecutive_falses = 0

    for i in range(len(row)):
        if row[i]:
            most_consecutive_falses = max(most_consecutive_falses,
                                          current_consecutive_falses)
            current_consecutive_falses = 0
        else:
            current_consecutive_falses += 1

    return most_consecutive_falses * cmPerPixel

def getThresholdImage(image_path):
    color_input = data.load(image_path)
    image = color.rgb2grey(color_input)
    thresh = threshold_mean(image)
    binary = image > thresh
    return binary

def get_average_x(points):
    average_x = 0.0
    for (x, y) in points:
        average_x += x
    average_x = average_x / len(points)
    return average_x

