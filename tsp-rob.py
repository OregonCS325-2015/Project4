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


# def calc_minDistance(list, startP):
#     minDist = 100000
#     pointIndex = 0  # initilaize
#
#     if startP > 0:
#
#         for i in range(0, startP - 1):
#             prevMinDist = minDist
#             # calculate the minimum distance
#             minDist = min(minDist, calc_distance(list[startP], list[i + 1]))
#             if minDist < prevMinDist:
#                 pointIndex = i + 1
#
#     # check from stp to end
#     for i in range(startP, len(list) - startP - 1):
#         prevMinDist = minDist
#         minDist = min(minDist, calc_distance(list[startP], list[i + 1]))
#         if minDist < prevMinDist:
#             pointIndex = i + 1
#
#     return minDist, pointIndex
#
#
# def genStartPoint(sortedList):
#
#     pointofreturn = ()
#     smallD = 99999999
#     for i in range(0, 10):
#
#         start_index = random.randrange (0, len(sortedList))
#         prevmin = smallD
#         mini, point = calc_minDistance(sortedList, start_index)
#         smallD = min (smallD, mini)
#         #store this point!
#         if smallD < prevmin:
#             pointofreturn = [mini, point, start_index]
#
#
#     return pointofreturn

zlist = read_file('tsp_test_cases/test-input-7.txt')

test = [(0, 50, 0), (0, 40, 1), (0, 10, 2)]
ysorted = sort_coordinates(zlist, 1)
xsorted = sort_coordinates(zlist, 0)

#print(px)
#print(py)

# ok here goes
# This path veriable is absolutly necessary
path = []
# i dont want it to be a global but it is for now
# The function, was built in a very liner fashion, thus there is repeated code but in the interest of time amd the complication nature of the
# function, I'm not going to change it to make use of repeated structures at this point.
# @ required is a sorted list


def spiralTSP(px, py):

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
        px.remove(lowy)      #remove
        py.pop(0)   #remove from end of x

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


    # print(temp)
    # print(px)
    # print(py)
    # print(path)

    if(len(px) > 1 ):
        spiralTSP(px, py)
    elif(len(px) == 1) :

        path.append(px[0])
        #dont think this is necessary but we'll see
        # if(len(py)>0):
        #     for i in range(0,len(py)):
        #         path.append(py[i])

    else:
        print('have a nice day')


#now call dat...
start = time.time()
spiralTSP(xsorted, ysorted)
stop = time.time()
duration = stop-start
#print ('It took this long to calculate points: %d ')%  duration #something wrong with this stupid line
#print ('It took this long to calculate %d ')% duration #something wrong with this stupid line

print('duration:')
print(duration)


# print path
# and time it took
print(path)
distance = 0
for i in range(0,len(path)):
    distance += path[i][2]

print(distance)

#checking lists for duplicates because list 3 is not working and I cannot explain it
dupCheck = set()
for i in range (0, len(xsorted)):
    dupCheck.add(xsorted[i])

if len(dupCheck) == len(xsorted):
    print ('they are equal')
#test = (999, 0 ,18)
#print (xsorted)