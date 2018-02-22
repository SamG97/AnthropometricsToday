import numpy as np

def calcCovarienceMatrix(nodes):
    return 0

def calcDist(a, b):
    return np.linalg.norm(a-b)


def calcNearestNeigbour(node, points):
    if len(points) == 0:
        return None
    point = np.array(node)
    dists = [calcDist(np.array(points[i]), point) for i in range(len(points))]
    distsCopy = dists.copy()
    distsCopy.sort()

    return 0
