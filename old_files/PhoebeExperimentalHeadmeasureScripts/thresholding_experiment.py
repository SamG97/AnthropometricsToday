from skimage import data, color, img_as_uint
from skimage.filters import threshold_mean
from skimage.io import imsave

cmPerPixel = 0.0458

base_location = "/Users/phoebenichols/AnthropometricsToday/" \
                "PhoebeExperimentalHeadmeasureScripts/images/"


def saveThresholdImage(imagepath):
    binary = getThresholdImage(imagepath)
    print(imagepath)
    location = 'output/thresholding/' + imagepath[
                                        len(base_location):]
    imsave(location, img_as_uint(binary))


def getThresholdImage(imagepath):
    color_input = data.load(imagepath)
    image = color.rgb2grey(color_input)
    thresh = threshold_mean(image)
    binary = image > thresh
    return binary


# TODO: discuss edge cases, for example where black at edge of image
def getHeadLength(imagepath):
    binary = getThresholdImage(imagepath)
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


print(getHeadLength("/Users/phoebenichols/AnthropometricsToday/"
                    "PhoebeExperimentalHeadmeasureScripts/"
                    "images/phoebe_profile_centered.jpg"))

saveThresholdImage("/Users/phoebenichols/AnthropometricsToday/"
                    "PhoebeExperimentalHeadmeasureScripts/"
                    "images/phoebe_profile_centered.jpg")
