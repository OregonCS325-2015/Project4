__author__ = 'Martha, Michael, and Robert'

import math
import heapq
import sys


# Reads the files
# @param a text file of space spearated numbers including an index
# @return three arrays one of x coordinates one of y, and one multi
# 0(n)
def read_file(name):
    x = []  # the values
    y = []
    z = []
    f = open(name, 'r')

    for i in f:
        index, a, b = i.split()
        x.append(int(a))
        y.append(int(b))
        z.append((int(a), int(b), int(index)))

    return x, y, z


# takes two lists one of x coordinates one of y, calculates distances between each point
# 0(n^2)
# @param a text file of space spearated numbers including an index
# @return one 2d array of distances
def calc_distance_matrix(x, y):
    matrix = [[0 for m in range(len(x))] for n in range(len(y))]

    for i in range(0, len(x)):

        for j in range(0, len(y)):
            # abs value because we don't want negative distances
            xdis = abs(x[i] - x[j])
            ydis = abs(y[i] - y[j])

            # dat hypotenuse - 3 figures
            dis = "%.3f" % math.sqrt(math.pow(xdis, 2) + math.pow(ydis, 2))
            matrix[i][j] = dis

    return matrix


# takes two coordinates, calculates distances between the point
# C
# @param crd  = a coordinate list
# @param i or j = a coordinate index i.e. [(438, 75), (381, 53)]  (438, 75) = 0
# @return one distance to three decimals
def calc_distance_point(crd, i, j):
    check1 = crd[i][0]
    check2 = crd[j][0]
    # abs value because we don't want negative distances
    xdis = abs(crd[i][0] - crd[j][0])
    ydis = abs(crd[i][1] - crd[j][1])

    # dat hypotenuse - 3 figures
    dis = "%.3f" % math.sqrt(math.pow(xdis, 2) + math.pow(ydis, 2))
    return dis


# takes two coordinates, calculates distances between the point
# C
# @param p1 p2 two points  = with an x and y coordt
# @return one distance to three decimals
def calc_distance(p1, p2):
    """
    :rtype : float
    """
    # abs value because we don't want negative distances
    xdis = abs(p1[0] - p2[0])
    ydis = abs(p1[1] - p2[1])

    # dat hypotenuse - 3 figures
    dis = "%.3f" % math.sqrt(math.pow(xdis, 2) + math.pow(ydis, 2))
    return dis


def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


# sorts a tuple
# @param crd  = a coordinate list
# @param a tuple
# @param v position 0 or 1 in the tuple (x or y)
# @return sorted tuple
def sort_coordinates(a, v):
    # set to look at opposite position for swapping
    # depending if we're sorting x's or y's
    if v == 0:
        l = 1
    else:
        l = 0

    a = sorted(a, key=lambda x: x[v])

    # bubble sorts the small sections where the sorted coordinate is the same
    for i in range(0, len(a)):
        # looks over the list swapping if the ys are larger
        for i in range(1, len(a)):
            if (a[i - 1][v] == a[i][v]) & (a[i - 1][l] > a[i][l]):
                # swap
                f, g = a[i - 1], a[i]
                a[i - 1], a[i] = g, f

    return a


# there will be four variables namely: xTop, xBottom, yTop, and YBottom that will be used to track current index from top and bottom in the two sorted lists
# There will be a list E that holds current connected edge list in contiguous order
# There will be a list v that is used to identify if specific vertex is already considered or not (0 for no or 1 for yes)
# @param tpos bpos = xTop or Xbottom or whaever, sorted list is which list you're working from
# @param E = visited edge lists
# @param V = verifier list
# @param sortedList = the x or y sorted list
def add_remaining(E, V, sortedList, tpos, bpos):
    # FOR EACH UNCONNECTED VERTEX, DETERMINE CONNECTION WITH LEAST ADDED COST (DISTANCE) AND CONNECT
    Addition = sys.maxsize

    while (tpos <= bpos):

        if V[tpos] == 0:

            # setup

            V[tpos] = 1
            vp = sortedList[tpos]  # coordinate pair of Xtop
            s = len(E)

            # loop
            for i in range(0, s - 1):

                d1 = calc_distance(vp[0], E[i])
                d2 = calc_distance(vp[0], E[i + 1])
                lofEdge = calc_distance(E[i], E[i + 1])
                newAddition = (d1 + d2 - lofEdge)

                ## if the new edge is awesome we do something with it
                if (newAddition < Addition):
                    Addition = newAddition
                    v1 = E[i]
                    v2 = E[i + 1]
                    idx = i + 1  # not sure what for

                i = i + 2  # not sure this what it's supposed to My Iterator is i in this loop, is this supposed to up that?

                # Connect vprime with v1 and v2 to create edges vprimev1 and vprimev2 and disconnect v1 from v2
                # IS THIS THE EQUVALEENT OF PUTTING vp between E[i] and E[i+1] then... but this is happeneing outside of your for loop in the doc and now I'm befuddeled.
                # IF it is the case the we only insert when the if stament is true then this can go above. in addtion it can be done then without setting the vars in the if stment. I followed the pseudo code and got lost

                E.insert(idx,
                         vp)  # CHECK THIS: it inserts before the point BUT IDEX IS NOT BEING SET OUT SIDE THE IF STMT

            tpos + 1  # increase teh check postion by 1

            # reset Addition
            Addition = sys.maxsize


x, y, z = read_file('tsp_test_cases/test-input-2.txt')

test = [(0, 50, 0), (0, 40, 1), (0, 10, 2)]
pyz = sort_coordinates(test, 0)
print(pyz)

print(calc_distance(test[0], test[1]))
