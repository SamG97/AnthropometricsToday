import face_recognition
from skimage import data, color
from skimage.filters import threshold_mean

cmPerPixel = 0.0458

def proccessImage(front_image_path, profile_image_path):
    return [getHeadLength(profile_image_path),
            getFaceWidth(front_image_path),
            getOcularWidth(front_image_path)]

#can use relative or full file path
def getOcularWidth(image_path):
    image = face_recognition \
        .load_image_file(image_path)

    face_landmarks_list = face_recognition.face_landmarks(image)

    if len(face_landmarks_list) == 0:
        # No face detected
        # TODO: discuss what to do here
        return 0

    ocularWidthOfAllFacesPresent = []

    for face in face_landmarks_list:
        right_eye_points = face.get('right_eye')
        left_eye_points = face.get('left_eye')

        left_avg = get_average_x(left_eye_points)
        right_avg = get_average_x(right_eye_points)

        ocularWidthOfAllFacesPresent += [(right_avg - left_avg) * cmPerPixel]
    result = max(ocularWidthOfAllFacesPresent)
    print("measured occular width as: " + str(result))
    return result

#can use relative or full file path
def getFaceWidth(image_path):
    image = face_recognition \
        .load_image_file(image_path)

    face_landmarks_list = face_recognition.face_landmarks(image)

    if len(face_landmarks_list) == 0:
        # No face detected
        # TODO: discuss what to do here
        return 0

    widthOfAllFacesPresent = []

    for face in face_landmarks_list:
        points = face.get('chin')
        x_points = []
        for (x, y) in points:
            x_points += [x]
        widthOfAllFacesPresent += [(max(x_points) - min(x_points)) * cmPerPixel]
    
    result = max(widthOfAllFacesPresent)
    print("measured face width as: " + str(result))
    return result

#needs full file path
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
    result = most_consecutive_falses * cmPerPixel
    print("measured profile length as: " + str(result))
    return result

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

def mini_test():
    front = "../../../" \
            "PhoebeExperimentalHeadmeasureScripts/images/" \
            "phoebe_face_glasses.jpg"
    profile = "/Users/phoebenichols/AnthropometricsToday/" \
            "PhoebeExperimentalHeadmeasureScripts/images/" \
            "phoebe_profile_centered.jpg"

    print(proccessImage(front, profile))
