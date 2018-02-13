import getHeadMeasurements

def testOccurlarWidth():
    image = "/Users/phoebenichols/AnthropometricsToday/" \
            "PhoebeExperimentalHeadmeasureScripts/images/" \
            "phoebe_face_glasses.jpg"
    result = getHeadMeasurements.getOcularWidth(image)
    assert(result > 4)
    assert(result < 10)
    print("test passed")

def testGetFaceWidth():
    image = "/Users/phoebenichols/AnthropometricsToday/" \
            "PhoebeExperimentalHeadmeasureScripts/images/" \
            "phoebe_face_glasses.jpg"
    result = getHeadMeasurements.getFaceWidth(image)
    assert(result > 10)
    assert(result < 20)
    print("test passed")

def testGetHeadLength():
    image = "/Users/phoebenichols/AnthropometricsToday/" \
            "PhoebeExperimentalHeadmeasureScripts/images/" \
            "phoebe_profile_centered.jpg"
    result = getHeadMeasurements.getHeadLength(image)
    assert (result > 6)
    assert (result < 14)
    print("test passed")


testOccurlarWidth()
testGetFaceWidth()
testOccurlarWidth()
