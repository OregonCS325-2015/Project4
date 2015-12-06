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

# #path[len(path)-1], points
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
#         if minDist <= prevMinDist:
#             pointIndex = i + 1
#
#     savedPoint = list[pointIndex]
#     list.pop(pointIndex)
#
#     return savedPoint

#path[len(path)-1], points
def calc_minDistance(startP, L):
    minDist = 100000
    pointIndex = 0  # initilaize


    # check from stp to end
    for i in range(0, len(L)):
        prevMinDist = minDist
        minDist = min(minDist, calc_distance(startP, L[i]))
        if minDist < prevMinDist:
            pointIndex = i
            savedPoint = L[pointIndex]
            #L.pop(pointIndex)

    return savedPoint



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
    tolerance = 100
    ###LEFT CYCLE
    if(len(px) != 0 and px != ''):
        #path.append(px[0])     #add to path
        #py.remove(px[0]) #remove same from y
        #px.pop(0)           #remove it


        #reset
        hix = px[len(px)-1]
        hiy = py[len(py)-1]
        lowx = px[0]
        lowy = py[0]

        #setdump Left
        temp = []
        # add the end of path
        #temp.append(path[len(path)-1])

        for i in range(0,len(px)):
        #     if (px[i][0] >= py[len(py)-1][0]+tolerance):
        #         break
        # for j in range(0,i):
        #     temp.append(px[j])

            if ((px[i][0] <= py[len(py)-1][0]+tolerance) & (px[i][1] >= px[0][1])-tolerance):
                temp.append(px[i])
            #     #px.remove(px[i])

        #ELSE sort the temp on the y
        temp = sort_coordinates(temp, 0)

        #dump it in the th path in order of increasing y
        for i in range(0,len(temp)):
            path.append(temp[i])
            px.pop(0)
            py.remove(temp[i])

    #TOPCYCLE
    #now add hiy
    if(len(px) != 0 and px != ''):
        # path.append(py[len(py)-1]) #add to path
        # px.remove(py[len(py)-1])
        # py.pop(len(py)-1)       #remove from end of y


        #setdump Top
        temp = []
        # add the end of path
        #temp.append(path[len(path)-1])
        #path.pop(len(path)-1)

        # for i in range(0,len(px)):
        #     if (px[i][1] >= px[len(py)-1][1]-tolerance):
        #         break
        # for j in range(0,i):
        #     temp.append(py[j])
        for i in range(0,len(px)):
            if (px[i][0] <= px[len(px)-1][0])& (px[i][1] >= px[len(px)-1][1]-tolerance):
                temp.append(px[i])


        #ELSE sort the temp on the x
        temp = sort_coordinates(temp, 0)
        #path.append(temp[0])
        #dump it in the th path in order of increasing x
        for i in range(1,len(temp)):
            path.append(temp[i])
            px.remove(temp[i])
            py.remove(temp[i])

    ###RIGHT CYCLE
    if(len(px) != 0 and px != ''):
        # path.append(px[len(px)-1])    #add to path
        # py.remove(px[len(px)-1])      #remove
        # px.pop(len(px)-1)           #remove from end of x
        #add end of path back on incase we shuffel
        temp = []
        # temp.append(path[len(path)-1])
        # path.pop(len(path)-1)

        for i in range(0,len(px)):
            if (px[i][0] >= py[0][0]-tolerance):
                break
        for j in range(0,i):
            temp.append(px[j])
        # #setdump RIGHT
        # temp = []
        # for i in range(0,len(px)):
        #     if (px[i][0] >= py[0][0]) & (px[i][1] <= px[len(px)-1][1] ):
        #         temp.append(px[i])
        #         py.remove(px[i])

        #ELSE sort the temp on the x
        temp = sort_coordinates(temp, 0)
        #path.append(temp[0])
        #dump it in the th path in order of decreasing y
        for i in range(len(temp)-1, -1, -1):
            path.append(temp[i])
            px.remove(temp[i])
            py.remove(temp[i])





    # ##adding the low y point
    # if(len(px) != 0 and px != ''):
    #     prevlow = py[0]
    #     path.append(py[0])       #add to path
    #     px.remove(py[0])      #remove
    #     py.pop(0)   #remove from end of x

    # #RightInside----------------------------------------------------
    # if(len(px) != 0 and px != ''):
    #     #setdump RIGHT
    #     temp = []
    #     for i in range(0,len(px)):
    #         if (px[i][0] >= py[0][0]) & (px[i][1] <= py[len(px)-1][1] ):
    #             temp.append(px[i])
    #             px.remove(px[i])
    #
    #     #ELSE sort the temp on the x
    #     temp = sort_coordinates(temp, 1)
    #
    #     #dump it in the th path in order of inccreasing y
    #     for i in range(0, len(temp)-1):
    #         path.append(temp[i])
    #         py.remove(temp[i])
    #
    #     prevx = px[len(px)-1]           #needed for next point
    #     path.append(px[len(px)-1])       #add next high x to path
    #     py.remove(px[len(px)-1])         #remove
    #     px.pop(len(px)-1)               #remove from end of x
    #
    # #-----------------------------------------------------------------
    #
    # #TOPInside----------------------------------------------------
    # if(len(px) != 0 and px != ''):
    #     #setdump RIGHT
    #     temp = []
    #     for i in range(0,len(px)):
    #         if (px[i][0] >= py[len(py)-1][0]) & (px[i][1] >= prevx[1] ):
    #             temp.append(px[i])
    #             px.remove(px[i])
    #
    #     #ELSE sort the temp on the x
    #     temp = sort_coordinates(temp, 0)
    #
    #     #dump it in the th path in order of inccreasing y
    #     for i in range(len(temp)-1, -1, -1):
    #         path.append(temp[i])
    #         py.remove(temp[i])
    #
    #     path.append(py[len(px)-1])       #add next high y to path
    #     px.remove(py[len(px)-1])         #remove from x
    #     py.pop(len(px)-1)               #remove from end of y
    #
    # #-----------------------------------------------------------------
    #
    # #LEFTInside----------------------------------------------------
    # if(len(px) != 0 and px != ''):
    #     #setdump RIGHT
    #     temp = []
    #     for i in range(0,len(px)):
    #         if (px[i][0] >= py[len(py)-1][0]) & (px[i][1] >= prevx[1] ):
    #             temp.append(px[i])
    #             px.remove(px[i])
    #
    #     #ELSE sort the temp on the x
    #     temp = sort_coordinates(temp, 0)
    #
    #     #dump it in the th path in order of inccreasing y
    #     for i in range(len(temp)-1, -1, -1):
    #         path.append(temp[i])
    #         py.remove(temp[i])
    #
    #     path.append(py[len(px)-1])       #add next high y to path
    #     px.remove(py[len(px)-1])         #remove from x
    #     py.pop(len(px)-1)               #remove from end of y

    #-----------------------------------------------------------------

    #BOTTOM CYCLE
    #now add py[0]
    if(len(px) != 0 and px != ''):
        # path.append(py[0])       #add to path
        # px.remove(py[0])      #remove
        # py.pop(0)   #remove from end of x

        #setdump Bottom
        temp = []
        for i in range(0,len(px)):
            if (px[i][0] <= py[0][0] ) & (px[i][1] <= px[0][1] ):
                temp.append(px[i])


        #ELSE sort the temp on the x
        temp = sort_coordinates(temp, 0)

        #dump it in the th path in order of decreasing x
        for i in range(len(temp)-1, -1, -1):
            path.append(temp[i])
            px.remove(temp[i])
            py.remove(temp[i])

    if(len(px) > 1 ):
        #spiralTSP(px, py)
        print(px)
    #elif(len(px) == 1) :

        # path.append(px[0])
        # dont think this is necessary but we'll see
        # if(len(py)>0):
        #     for i in range(0,len(py)):
        #         path.append(py[i])

    else:
        print('have a nice day')
#now call dat...
# start = time.time()
# spiralTSP(xsorted, ysorted)
# stop = time.time()
# duration = stop-start
#print ('It took this long to calculate points: %d ')%  duration #something wrong with this stupid line
#print ('It took this long to calculate %d ')% duration #something wrong with this stupid line


def bs():
    factor = int(len(xsorted)/4) # for dividing up the grid

    xslice = xsorted[0:factor]
    yslice = ysorted[0:factor]

    xset = set(xslice)
    yset = set(yslice)

    #get the matching points and resort
    points = sort_coordinates(list(xset & yset), 1)
    print (points)

    #put lowest in a list
    path = []
    path.append(points[0])
    points.pop(0)

    for i in range(0, len(points)):
        path.append(calc_minDistance(path[len(path)-1], points))  # start at the end of the path calc to al other points
        points.remove(path[len(path)-1])
        print (points)
        print(path)

    pathset = set(path)


zlist = read_file('tsp_test_cases/tsp_example_1.txt')
test = [(0, 50, 0), (0, 40, 1), (0, 10, 2)]
ysorted = sort_coordinates(zlist, 1)
xsorted = sort_coordinates(zlist, 0)

bs()

print(path)
# update xsotred and y sorted
# new = list( set(xsorted)&set(ysorted) )
# ysorted = sort_coordinates(new, 1)
# xsorted = sort_coordinates(new, 0)
#
# print(new)
# print(len(new))

#union = list(xset.intersection(yset))

#print(union)
#
#
# for i in range(0, factor-1):            #n/5 elements
#     xset.add(xsorted[i])
#     yset.add(ysorted[i])


#print(xset)
#print(yset)

#
# union = list(xset.intersection(yset))
# union2 = xset.symmetric_difference(yset)
#
# print(union)

#
# print('duration:')
# print(duration)


# print path
# and time it took
# print(path)
# distance = 0
# for i in range(0,len(path)-1):
#     distance += calc_distance(path[i],path[i+1])
#
# print(distance)
#
# #checking lists for duplicates because list 3 is not working and I cannot explain it
# dupCheck = set()
# for i in range (0, len(xsorted)):
#     dupCheck.add(xsorted[i])
#
# if len(dupCheck) == len(xsorted):
#     print ('they are equal')
