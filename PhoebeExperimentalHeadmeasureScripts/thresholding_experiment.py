from skimage import data, color, img_as_uint
from skimage.filters import threshold_mean
from skimage.io import imsave
from skimage.viewer import ImageViewer

base_location = "/Users/phoebenichols/AnthropometricsToday/PhoebeExperimentalHeadmeasureScripts/images/"

def thresholdImage(imagepath):
    color_input = data.load(imagepath)
    image = color.rgb2grey(color_input)
    # Threshold is mean intensity
    thresh = threshold_mean(image)
    binary = image > thresh
    print(imagepath)
    location = 'output/thresholding/' + imagepath[
                                        len(base_location):]
    imsave(location, img_as_uint(binary))

thresholdImage("/Users/phoebenichols/AnthropometricsToday/PhoebeExperimentalHeadmeasureScripts/images/phoebe_profile_centered.jpg")

