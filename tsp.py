__author__ = 'Martha, Michael, and Robert'

import math
import heapq


#Reads the files
#@param a text file of space spearated numbers including an index
#@return three arrays one of x coordinates one of y, and one multi
# 0(n)
def read_file(name):
    x = [] # the values
    y = []
    z = []
    f = open( name, 'r')

    for i in f:
        index, a, b = i.split()
        x.append(int(a))
        y.append(int(b))
        z.append((int(a), int(b), int(index)))

    return x, y, z

#takes two lists one of x coordinates one of y, calculates distances between each point
# 0(n^2)
#@param a text file of space spearated numbers including an index
#@return one 2d array of distances
def calc_distance_matrix(x, y):

    matrix = [[0 for m in range(len(x))] for n in range(len(y)) ]

    for i in range(0, len(x)):

        for j in range(0, len(y)):

            #abs value because we don't want negative distances
            xdis = abs(x[i] - x[j])
            ydis = abs(y[i] - y[j])

            # dat hypotenuse - 3 figures
            dis = "%.3f" % math.sqrt(math.pow(xdis,2) + math.pow(ydis,2) )
            matrix[i][j]= dis


    return matrix

#takes two coordinates, calculates distances between the point
# C
#@param crd  = a coordinate list
#@param i or j = a coordinate index i.e. [(438, 75), (381, 53)]  (438, 75) = 0
#@return one distance to three decimals
def calc_distance_point(crd, i, j):

    check1 = crd[i][0];
    check2 = crd[j][0];
    #abs value because we don't want negative distances
    xdis = abs(crd[i][0] - crd[j][0])
    ydis = abs(crd[i][1] - crd[j][1])

    # dat hypotenuse - 3 figures
    dis = "%.3f" % math.sqrt(math.pow(xdis,2) + math.pow(ydis,2) )
    return dis


def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


# sorts a tuple
#@param crd  = a coordinate list
#@param a tuple
#@param v position 0 or 1 in the tuple (x or y)
#@return sorted tuple
def sort_coordinates(a, v):

    # set to look at opposite position for swapping
    # depending if we're sorting x's or y's
    if v == 0:
        l = 1
    else:
        l = 0

    a = sorted(z, key=lambda x: x[v])

    #looks over the list swapping if the ys are larger
    for i in range(0,len(a)-1):
        if (a[i][v] == a[i+1][v]) & (a[i][l] > a[i+1][l]):
            #swap
            f,g = a[i], a[i+1]
            a[i], a[i+1]= g,f

    return a



x,y,z = read_file('tsp_test_cases/test-input-2.txt')

pyz = sort_coordinates(z,0)
print (z)
print(pyz)

