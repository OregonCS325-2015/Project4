__author__ = 'Martha, Michael, and Robert'

import math
import heapq
import sys
import time
import random


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
        #x.append(int(a))
        #y.append(int(b))
        z.append((int(a), int(b), int(index)))

    return z


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
    # """
    # :rtype : float
    # """
    # abs value because we don't want negative distances
    xdis = abs(p1[0] - p2[0])
    ydis = abs(p1[1] - p2[1])

    # dat hypotenuse - 3 figures
    #dis = "%.3f" % math.sqrt(math.pow(xdis, 2) + math.pow(ydis, 2))
    dis = int( math.sqrt(math.pow(xdis, 2) + math.pow(ydis, 2)))

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

# #Create outer cycle
# #create edge list tuple
# #create vertex tracking list
# #create path tracking list
def algorithm(l):

    size = len(l)

    list1 = sort_coordinates(l, 0)
    list2 = sort_coordinates(l, 1)
    xTop = 0
    xBottom = size - 1
    yTop = 0
    yBottom = size - 1

    vertexList = [0] * size
    path = [0] * size
    pathIndex = 0
    smallXsmallY = list1[xTop]
    E = []

    while (list1[xTop][0] == list1[xTop + 1][0]):
        E.append((int(list1[xTop][0]), int(list1[xTop][1]), int(list1[xTop][2])))
        E.append((int(list1[xTop + 1][0]), int(list1[xTop + 1][1]), int(list1[xTop + 1][2])))
        path[pathIndex] = list1[xTop][2]
        pathIndex = pathIndex + 1
        path[pathIndex] = list1[xTop + 1][2]
        if (vertexList[list1[xTop][2] - 1] == 0):
            vertexList[list1[xTop][2] - 1] = 1
        if (vertexList[list1[xTop + 1][2] - 1] == 0):
            vertexList[list1[xTop + 1][2] - 1] = 1
        xTop = xTop + 1

    smallXlargeY = list1[xTop]
    if (vertexList[list1[xTop][2] - 1] == 0):
        vertexList[list1[xTop][2] - 1] = 1

    largeYlargeX = list2[yBottom]
    while (list2[yBottom][1] == list2[yBottom - 1][1]):
        E.append((int(list2[yBottom][0]), int(list2[yBottom][1]), int(list2[yBottom][2])))
        E.append((int(list2[yBottom - 1][0]), int(list2[yBottom - 1][1]), int(list2[yBottom - 1][2])))
        if (vertexList[list2[yBottom][2] - 1] == 0):
            vertexList[list2[yBottom][2] - 1] = 1
        if (vertexList[list2[yBottom - 1][2] - 1] == 0):
            vertexList[list2[yBottom - 1][2] - 1] = 1
        yBottom = yBottom - 1
    largeYsmallX = list2[yBottom + 1]

    if (smallXlargeY != largeYsmallX):
        E.append((int(list1[xTop][0]), int(list1[xTop][1]), int(list1[xTop][2])))

        E.append((int(list2[yBottom][0]), int(list2[yBottom][1]), int(list2[yBottom][2])))
    yBot = yBottom
    pathIndex = pathIndex + 1
    while (yBot < size):
        path[pathIndex] = list2[yBot][2]
        pathIndex = pathIndex + 1
        yBot = yBot + 1

    largeXlargeY = list1[xBottom]
    while (list1[xBottom][0] == list1[xBottom - 1][0]):
        E.append((int(list1[xBottom][0]), int(list1[xBottom][1]), int(list1[xBottom][2])))
        E.append((int(list1[xBottom - 1][0]), int(list1[xBottom - 1][1]), int(list1[xBottom - 1][2])))
        if (vertexList[list1[xBottom][2] - 1] == 0):
            vertexList[list1[xBottom][2] - 1] = 1
        if (vertexList[list1[xBottom - 1][2] - 1] == 0):
            vertexList[list1[xBottom - 1][2] - 1] = 1

        path[pathIndex] = list1[xBottom][2]
        pathIndex = pathIndex + 1
        path[pathIndex] = list1[xBottom - 1][2]
        xBottom = xBottom - 1

    largeXsmallY = list1[xBottom]

    if (largeXlargeY != largeYlargeX):
        E.append((largeYlargeX))

        E.append((largeXlargeY))

    smallYsmallX = list2[yTop]

    while (list2[yTop][1] == list2[yTop + 1][1]):
        E.append((int(list2[yTop][0]), int(list2[yTop][1]), int(list2[yTop][2])))
        E.append((int(list2[yTop + 1][0]), int(list2[yTop + 1][1]), int(list2[yTop + 1][2])))

        if (vertexList[list2[yTop][2] - 1] == 0):
            vertexList[list2[yTop][2] - 1] = 1
        if (vertexList[list2[yTop + 1][2] - 1] == 0):
            vertexList[list2[yTop + 1][2] - 1] = 1
        yTop = yTop + 1

    smallYlargeX = list2[yTop]
    if (vertexList[list2[yTop][2] - 1] == 0):
        vertexList[list2[yTop][2] - 1] = 1

    if (largeXsmallY != smallYlargeX):
        E.append((largeXsmallY))

        E.append((smallYlargeX))

    if (smallYsmallX != smallXsmallY):
        E.append((smallYsmallX))

        E.append((smallXsmallY))

    yTo = yTop
    pathIndex = pathIndex + 1
    while (yTo >= 0):
        path[pathIndex] = list2[yTo][2]
        pathIndex = pathIndex + 1
        yTo = yTo - 1

    print
    E[0:len(E)]
    print
    vertexList[0:len(vertexList)]
    print
    path[0:len(path)]







# there will be four variables namely: xTop, xBottom, yTop, and yBottom that will be used to track current index from top and bottom in the two sorted lists
# There will be a list E that holds current connected edge list in contiguous order
# There will be a list v that is used to identify if specific vertex is already considered or not (0 for no or 1 for yes)
# @param tpos bpos = xTop or Xbottom or whaever, sorted list is which list you're working from
# @param E = visited edge lists
# @param V = verifier list
# @param sortedList = the x or y sorted list
def add_remaining(E, V, sortedList, tpos, bpos):
    # FOR EACH UNCONNECTED VERTEX, DETERMINE CONNECTION WITH LEAST ADDED COST (DISTANCE) AND CONNECT

    while tpos <= bpos:
        addition = sys.maxsize

        if V[tpos] == 0:

            # setup

            V[tpos] = 1
            vp = sortedList[tpos]  # coordinate pair of Xtop
            s = len(E)
            idx = 0
            v1 = 0
            v2 = 0

            # loop
            for i in range(0, s - 1):
                # calc edges between all 3 points
                d1 = calc_distance(vp[0], E[i])
                d2 = calc_distance(vp[0], E[i + 1])
                lofEdge = calc_distance(E[i], E[i + 1])
                newAddition = (d1 + d2 - lofEdge)

                # if the new edge is awesome we do something with it
                if newAddition < addition:
                    addition = newAddition
                    v1 = E[i]
                    v2 = E[i + 1]
                    idx = i + 1  # not sure what for

            # Connect vprime with v1 and v2 to create edges vprimev1 and vprimev2 and disconnect v1 from v2
            # IS THIS THE EQUIVALENT OF PUTTING vp between E[i] and E[i+1] then... but this is happening outside of your for loop in the doc and now I'm befuddeled.
            # IF it is the case the we only insert when the if statement is true then this can go above. in addition it can be done then without setting the vars in the if stment. I followed the pseudo code and got lost

            E.insert(idx,
                     vp)  # CHECK THIS: it inserts before the point BUT IDEX IS NOT BEING SET OUT SIDE THE IF STMT

        tpos += 1  # increase the check position by 1


def calc_minDistance(list, startP):
    minDist = 100000
    pointIndex = 0  # initilaize

    if startP > 0:

        for i in range(0, startP - 1):
            prevMinDist = minDist
            # calculate the minimum distance
            minDist = min(minDist, calc_distance(list[startP], list[i + 1]))
            if minDist < prevMinDist:
                pointIndex = i + 1

    # check from stp to end
    for i in range(startP, len(list) - startP - 1):
        prevMinDist = minDist
        minDist = min(minDist, calc_distance(list[startP], list[i + 1]))
        if minDist < prevMinDist:
            pointIndex = i + 1

    return minDist, pointIndex


def genStartPoint(sortedList):

    pointofreturn = ()
    smallD = 99999999
    for i in range(0, 10):

        start_index = random.randrange (0, len(sortedList))
        prevmin = smallD
        mini, point = calc_minDistance(sortedList, start_index)
        smallD = min (smallD, mini)
        #store this point!
        if smallD < prevmin:
            pointofreturn = [mini, point, start_index]


    return pointofreturn

zlist = read_file('tsp_test_cases/test-input-robtest.txt')

test = [(0, 50, 0), (0, 40, 1), (0, 10, 2)]
py = sort_coordinates(zlist, 1)
px = sort_coordinates(zlist, 0)

print(px)
print(py)
path = []
def shit():

    ###LEFT CYCLE
    if(len(px) != 0 or px != ''):
        path.append(px[0])     #add to path
        py.remove(px[0]) #remove same from y
        px.pop(0)           #remove it


        #reset
        hix = px[len(px)-1]
        hiy = py[len(py)-1]
        lowx = px[0]
        lowy = py[0]

        #setdump Left
        temp = []
        for i in range(0,len(px)):
            if (px[i][0] < hiy[0]) & (px[i][1] > lowx[1]):
                temp.append(px[i])
                py.remove(px[i])

        #ELSE sort the temp on the y
        temp = sort_coordinates(temp, 1)

        #dump it in the th path in order of increasing y
        for i in range(0,len(temp)):
            path.append(temp[i])
            px.remove(temp[i])

    #TOPCYCLE
    #now add hiy
    if(len(px) != 0 or px != ''):
        path.append(hiy) #add to path
        py.pop(len(py)-1)       #remove from end of y
        px.remove(hiy)


        # #reset
        # hix = px[len(px)-1]
        # hiy = py[len(py)-1]
        # lowx = px[0]
        # lowy = py[0]

        #setdump Top
        temp = []
        for i in range(0,len(px)):
            if (px[i][0] > hiy[0]) & (px[i][1] > hix[1]):
                temp.append(px[i])
                py.remove(px[i])

        #ELSE sort the temp on the x
        temp = sort_coordinates(temp, 0)

        #dump it in the th path in order of increasing y
        for i in range(0,len(temp)):
            path.append(temp[i])
            px.remove(temp[i])


    ###RIGHT CYCLE
    #now add hix
    if(len(px) != 0 or px != ''):
        path.append(hix)       #add to path
        py.remove(hix)      #remove
        px.pop(len(px)-1)   #remove from end of x


        # #reset
        # hix = px[len(px)-1]
        # hiy = py[len(py)-1]
        # lowx = px[0]
        # lowy = py[0]

        #setdump RIGHT
        temp = []
        for i in range(0,len(px)):
            if (px[i][0] > lowy[0]) & (px[i][1] < hix[1]):
                temp.append(px[i])
                py.remove(px[i])

        #ELSE sort the temp on the x
        temp = sort_coordinates(temp, 1)

        #dump it in the th path in order of decreasing y
        for i in range(len(temp)-1, -1, -1):
            path.append(temp[i])
            px.remove(temp[i])

    #BOTTOM CYCLE
    #now add lowy
    if(len(px) != 0 or px != ''):
        path.append(lowy)       #add to path
        py.pop(0)   #remove from end of x
        px.remove(lowy)      #remove

        # hix = px[len(px)-1]
        # hiy = py[len(py)-1]
        # lowx = px[0]
        # lowy = py[0]

        #setdump Bottom
        temp = []
        for i in range(0,len(px)):
            if (px[i][0] < lowy[0]) & (px[i][1] < lowx[1]):
                temp.append(px[i])
                py.remove(px[i])

        #ELSE sort the temp on the x
        temp = sort_coordinates(temp, 0)

        #dump it in the th path in order of decreasing x
        for i in range(len(temp)-1, -1, -1):
            path.append(temp[i])
            px.remove(temp[i])


    print(temp)
    print(px)
    print(py)
    print(path)

    if(len(px) >0 or px != ''):
        shit()
    else:
        if(len(py)>0):
            for i in range(0,len(py)):
                path.append(py[i])
        print('have a nice day')

shit()


#HELD -KARP
##print(calc_distance(zlist[0], zlist[1]))
# #print (calc_minDistance(pyx, 0))
# path = set()
# dist = []
# for i in range(0, 20):
#     a = genStartPoint(zlist)
#
#     tup = (a[1], a[2])
#     zlist.pop(a[2])
#     zlist.pop(a[1])
#     path.add(tup)
#     dist.append(a[0])
#
#     #path.add(a)
#     #b = genStartPoint(zlist)
#
#     print(a)
#
# print(path)
# print(dist)
#
# print(len(zlist))
# print(zlist[1366])
# print(zlist[1258])
#
# a = calc_minDistance(zlist, 1258)
# print (a)