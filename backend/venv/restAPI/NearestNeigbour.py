import numpy as np
from restAPI.DataBaseScript import getAllMeasurements

def discardNone(a):
    b = []
    for i in range(len(a)):
        isFull = True
        for j in range(len(a[i])):
            if a[i][j] == None:
                isFull = False
        if isFull:
            b.append(a[i])
    return b

studentList = getAllMeasurements()
students = [{studentList.getall()[j][i][0]: studentList.getall()[j][i][1] for i in range(len(studentList.getall()[j]))}
           for j in range(len(studentList.getall()))]
dists = np.array(discardNone([[students[i]['Head_length'], students[i]['Face_breadth'], students[i]['Face_iobreadth']] for i in
         range(len(students))]))

elipseMatrix = np.cov(dists, rowvar=False)#, rowvar = False)

try:
    elipseMatrix = np.linalg.inv(elipseMatrix)
except:
    elipseMatrix = np.identity(len(elipseMatrix))

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
    return np.random.choice(range(len(dists)), 1,  p = list(probs))[0]

def calcNearestNeigbour(node, points):
    if len(points) == 0:
       return None
    point = np.array(node)
    points = discardNone(points)
    dists = [calcDist(np.array(points[i]), point) for i in range(len(points))]
    return getIndex(dists)

if __name__ == '__main__':
    #tests
    print(elipseMatrix)
    print(calcDist(np.array([0,0,0]), np.array([1,2,3])))
    print(getIndex([100,300,500,2000,0.1,2000]))
    print(calcNearestNeigbour([2,4,5],[[1,4,5],[2,3,2],[2,2,2],[4,2,3],[1,1,1]]))