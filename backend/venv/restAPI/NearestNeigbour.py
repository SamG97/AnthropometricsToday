import numpy as np
from restAPI.DataBaseScript import getAllMeasurements

def calcCovarienceMatrix():
    studentList = getAllMeasurements()
    students = [{studentList.get()[j][i][0]: studentList.getall()[j][i][1] for i in range(len(studentList.getall()[j]))}
                for j in range(len(studentList.getall()))]
    dists = np.array([np.array([students[i]['Head_length'], students[i]['Face_breadth'], students[i]['Face_iobreadth']]) for i in
             range(len(students))])
    return np.cov(dists)

elipseMatrix = np.linalg.inv(calcCovarienceMatrix())

def calcDist(a, b):
    ab = b-a
    return np.sqrt(np.dot(np.dot(np.transpose(ab),elipseMatrix), ab))

def sigmoid(x):
    return 1/(1+np.exp(-x))

def getIndex(dists):
    sum = 0
    for i in range(len(dists)):
        sum += 1-sigmoid(dists[i])
    probs = [(1-sigmoid(dists[i]))/sum for i in range(len(dists))]
    return np.random.choice(range(len(dists)), 1,  p = list(probs))

#def calcNearestNeigbour(node, points):
#    if len(points) == 0:
#        return None
#    point = np.array(node)
#    dists = [calcDist(np.array(points[i]), point) for i in range(len(points))]
#    return getIndex(dists)

if __name__ == '__main__':
    #tests
    print(elipseMatrix)
    print(getIndex([100,300,500,2000,0.1,2000]))
