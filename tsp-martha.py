import sys
import math
import time
import getopt

#adapted from http://www.tutorialspoint.com/python/python_command_line_arguments.htm
def cmd_line_io(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=", "ofile="])
	except getopt.GetoptError:
		print ('p4.py -i <inputfile> -o <outputfile>')
		sys.exit(2)
	for opt, arg in opts:
		#help
		if opt == '-h':
			print ('p4.py -i <inputfile> ')
			sys.exit()

		#input file
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg

	return inputfile, outputfile

	print ('Input file is "', inputfile)
	print ('Output file is "', outputfile)


def read_file(name):

    z = []
    f = open(name, 'r')

    for i in f:
        index, a, b = i.split()
        z.append((int(a), int(b), int(index)))

    return z


def calc_distance(p1, p2):
    xdis = abs(p1[0] - p2[0])
    ydis = abs(p1[1] - p2[1])

    # dat hypotenuse - 3 figures
	# dis = "%.3f" % math.sqrt(math.pow(xdis, 2) + math.pow(ydis, 2))
    dis = float(math.sqrt(math.pow(xdis, 2) + math.pow(ydis, 2)))

    return dis


def sort_coordinates(a, v):
    # set to look at opposite position for swapping
    # depending if we're sorting x's or y's
    if v == 0:
        l = 1
    else:
        l = 0

    a = sorted(z, key=lambda x: x[v])
    #    print a[0:len(a)]
    for i in range(0, len(a)):
        # looks over the list swapping if the ys are larger
        for i in range(1, len(a)):
            if (a[i - 1][v] == a[i][v]) & (a[i - 1][l] > a[i][l]):
                # swap
                f, g = a[i - 1], a[i]
                a[i - 1], a[i] = g, f

    return a


def algorithm(l):
    size = len(l)
    list1 = sort_coordinates(l, 0)
    list2 = sort_coordinates(l, 1)
    xTop = 0
    xBottom = size - 1
    yTop = 0
    yBottom = size - 1

    vertexList = [0] * size

    # find the left most vertex(vertices). Connect if more than one
    smallXsmallY = list1[xTop]
    if (vertexList[list1[xTop][2]] == 0):
        vertexList[list1[xTop][2]] = 1

    E = []

    while (list1[xTop][0] == list1[xTop + 1][0]):
        E.append((int(list1[xTop][0]), int(list1[xTop][1]), int(list1[xTop][2])))
        E.append((int(list1[xTop + 1][0]), int(list1[xTop + 1][1]), int(list1[xTop + 1][2])))
        if (vertexList[list1[xTop][2]] == 0):
            vertexList[list1[xTop][2]] = 1
        if (vertexList[list1[xTop + 1][2]] == 0):
            vertexList[list1[xTop + 1][2]] = 1
        xTop = xTop + 1

    smallXlargeY = list1[xTop]
    if (vertexList[list1[xTop][2]] == 0):
        vertexList[list1[xTop][2]] = 1

    # find the top most vertex(ices). Connect if more than one
    largeYlargeX = list2[yBottom]
    if (vertexList[list2[yBottom][2]] == 0):
        vertexList[list2[yBottom][2]] = 1

    while (list2[yBottom][1] == list2[yBottom - 1][1]):
        E.append((int(list2[yBottom][0]), int(list2[yBottom][1]), int(list2[yBottom][2])))
        E.append((int(list2[yBottom - 1][0]), int(list2[yBottom - 1][1]), int(list2[yBottom - 1][2])))
        if (vertexList[list2[yBottom][2]] == 0):
            vertexList[list2[yBottom][2]] = 1
        if (vertexList[list2[yBottom - 1][2]] == 0):
            vertexList[list2[yBottom - 1][2]] = 1
        yBottom = yBottom - 1

    # if (yBottom==size-1):
    #	yBottom=yBottom-1
    #     yBottom=yBottom+1
    largeYsmallX = list2[yBottom]
    #     largeYsmallX=list2[yBottom+1]

    if (vertexList[list2[yBottom][2]] == 0):
        vertexList[list2[yBottom][2]] = 1

    # yBottom=yBottom+1

    # connect left most vertex (if more than one,
    # top vertex of left most vertices) WITH top more vertex
    # (if more than one, left vertex of top most vertices)
    # unless it turns out to be the same vertex
    if (smallXlargeY != largeYsmallX):
        E.append((smallXlargeY))
        E.append((largeYsmallX))

    largeXlargeY = list1[xBottom]
    if (vertexList[list1[xBottom][2]] == 0):
        vertexList[list1[xBottom][2]] = 1

    while (list1[xBottom][0] == list1[xBottom - 1][0]):
        E.append((int(list1[xBottom][0]), int(list1[xBottom][1]), int(list1[xBottom][2])))
        E.append((int(list1[xBottom - 1][0]), int(list1[xBottom - 1][1]), int(list1[xBottom - 1][2])))
        if (vertexList[list1[xBottom][2]] == 0):
            vertexList[list1[xBottom][2]] = 1
        if (vertexList[list1[xBottom - 1][2]] == 0):
            vertexList[list1[xBottom - 1][2]] = 1

        xBottom = xBottom - 1

    largeXsmallY = list1[xBottom]

    if (largeXlargeY != largeYlargeX):
        E.append((largeYlargeX))

        E.append((largeXlargeY))

    smallYsmallX = list2[yTop]

    while (list2[yTop][1] == list2[yTop + 1][1]):
        E.append((int(list2[yTop][0]), int(list2[yTop][1]), int(list2[yTop][2])))
        E.append((int(list2[yTop + 1][0]), int(list2[yTop + 1][1]), int(list2[yTop + 1][2])))

        if (vertexList[list2[yTop][2]] == 0):
            vertexList[list2[yTop][2]] = 1
        if (vertexList[list2[yTop + 1][2]] == 0):
            vertexList[list2[yTop + 1][2]] = 1
        yTop = yTop + 1

    smallYlargeX = list2[yTop]
    if (vertexList[list2[yTop][2]] == 0):
        vertexList[list2[yTop][2]] = 1

    if (largeXsmallY != smallYlargeX):
        E.append((largeXsmallY))

        E.append((smallYlargeX))

    if (smallYsmallX != smallXsmallY):
        E.append((smallYsmallX))
        E.append((smallXsmallY))
    cost = 0
    i = 0
    while i < (len(E) - 1):
        length = calc_distance(E[i], E[i + 1])
        # 	print E[i][2]
        # 	print E[i+1][2]
        cost = float(cost + length)
        #	print ("cost: %d" %cost)
        i = i + 2

    # print E[0:len(E)]
    xTop = xTop + 1
    xBottom = xBottom - 1
    yTop = yTop + 1
    yBottom = yBottom - 1

    # for i in range (0, size):
    while xTop <= xBottom:
        addition = sys.maxsize
        if xTop <= xBottom:
            # print vertexList[list1[xTop][2]-1]
            if vertexList[list1[xTop][2]] == 0:
                vertexList[list1[xTop][2]] = 1
                newV = list1[xTop]
                # print list1[xTop][2]
                s = len(E)
                i = 0
                while (i <= s - 1):
                    d1 = calc_distance(newV, E[i])
                    d2 = calc_distance(newV, E[i + 1])
                    lenEdge = calc_distance(E[i], E[i + 1])
                    newAddition = d1 + d2 - lenEdge
                    if newAddition < addition:
                        addition = newAddition
                        v1 = E[i]
                        v2 = E[i + 1]
                        #	print ("additon: %d" %addition)
                        #			print "\n"
                        #			print newV
                        #			print v1
                        #			print v2
                        idx = i + 1
                    i = i + 2
                # print "\n"
                #		print"ONE"
                #		print newV
                #		print v1
                #		print v2


                E.append((E[idx]))
                E[idx] = newV
                E.append((newV))
                cost = float(cost + addition)
            xTop = xTop + 1
        # print E[0:len(E)]


        addition = sys.maxsize
        while list1[xTop][0] == list1[xTop - 1][0]:
            if xTop <= xBottom:
                # print vertexList[list1[xTop][2]-1]
                if vertexList[list1[xTop][2]] == 0:
                    vertexList[list1[xTop][2]] = 1
                    newV = list1[xTop]
                    # print list1[xTop][2]
                    s = len(E)
                    i = 0
                    while (i <= s - 1):
                        d1 = calc_distance(newV, E[i])
                        d2 = calc_distance(newV, E[i + 1])
                        lenEdge = calc_distance(E[i], E[i + 1])
                        newAddition = d1 + d2 - lenEdge
                        if newAddition < addition:
                            addition = newAddition
                            v1 = E[i]
                            v2 = E[i + 1]
                            #			print ("additon: %d" %addition)
                            #			print "\n"
                            #			print newV
                            #			print v1
                            #			print v2

                            idx = i + 1
                        i = i + 2
                    # print "\n"
                    #		print "TWO"
                    #		print newV
                    #		print v1
                    #		print v2


                    E.append((E[idx]))
                    E[idx] = newV
                    E.append((newV))
                    cost = float(cost + addition)
                xTop = xTop + 1
            # print E[0:len(E)]

        addition = sys.maxsize
        # m=list1[xBottom][0]
        # n=list1[xBottom-1][0]
        # while list1[xBottom][0]==list1[xBottom-1][0]:
        if xBottom >= xTop:
            # print xBottom
            # print xTop
            # print vertexList[list1[xBottom][2]-1]
            if vertexList[list1[xBottom][2]] == 0:
                vertexList[list1[xBottom][2]] = 1
                newV = list1[xBottom]
                # print list1[xBottom][2]
                s = len(E)
                i = 0
                while (i <= s - 1):
                    d1 = calc_distance(newV, E[i])
                    d2 = calc_distance(newV, E[i + 1])

                    lenEdge = calc_distance(E[i], E[i + 1])
                    newAddition = d1 + d2 - lenEdge
                    if newAddition < addition:
                        addition = newAddition
                        v1 = E[i]
                        v2 = E[i + 1]
                        #			print ("additon: %d" %addition)
                        #			print "\n"
                        #			print newV
                        #			print v1
                        #			print v2

                        idx = i + 1
                    i = i + 2

                # print "\n"
                #		print "THREE"
                #		print newV
                #		print v1
                #		print v2


                E.append((E[idx]))
                E[idx] = newV
                E.append((newV))
                cost = float(cost + addition)
            xBottom = xBottom - 1
        # print E[idx-1]
        #	     print E[idx]
        #	     print ("idxThree: %d" %idx)
        #	     print E[0:len(E)]




        while list1[xBottom][0] == list1[xBottom + 1][0]:
            if xBottom >= xTop:
                if vertexList[list1[xBottom][2]] == 0:
                    vertexList[list1[xBottom][2]] = 1
                    newV = list1[xBottom]
                    # print list1[xBottom][2]
                    s = len(E)
                    i = 0
                    while (i <= s - 1):
                        d1 = calc_distance(newV, E[i])
                        d2 = calc_distance(newV, E[i + 1])

                        lenEdge = calc_distance(E[i], E[i + 1])
                        newAddition = d1 + d2 - lenEdge
                        if newAddition < addition:
                            addition = newAddition
                            v1 = E[i]
                            v2 = E[i + 1]
                            #			print ("additon: %d" %addition)
                            #			print "\n"
                            #			print newV
                            #			print v1
                            #			print v2

                            idx = i + 1
                        i = i + 2

                    # print "\n"
                    #		print "FOUR"
                    #		print newV
                    #		print v1
                    #		print v2

                    #		print E[0:len(E)]
                    #		print E[idx]
                    E.append((E[idx]))
                    E[idx] = newV
                    E.append((newV))
                    #		print ("idxFour: %d" %idx)
                    cost = float(cost + addition)
                xBottom = xBottom - 1
            #	     print E[0:len(E)]

        addition = sys.maxsize
        # while list1[yTop][1]==list1[yTop+1][1]:
        if yTop <= yBottom:
            # print vertexList[list1[yTop][2]-1]
            if vertexList[list2[yTop][2]] == 0:
                vertexList[list2[yTop][2]] = 1
                newV = list2[yTop]
                # print list1[yTop][2]
                s = len(E)
                i = 0
                while (i <= s - 1):
                    d1 = calc_distance(newV, E[i])
                    d2 = calc_distance(newV, E[i + 1])
                    lenEdge = calc_distance(E[i], E[i + 1])
                    newAddition = d1 + d2 - lenEdge
                    if newAddition < addition:
                        addition = newAddition

                        v1 = E[i]
                        v2 = E[i + 1]
                        #			print ("additon: %d" %addition)
                        #			print "\n"
                        #			print newV
                        #			print v1
                        #			print v2

                        idx = i + 1
                    i = i + 2

                # print "\n"
                #		print "FIVE"
                #		print newV
                #		print v1
                #		print v2


                E.append((E[idx]))
                E[idx] = newV
                E.append((newV))
                cost = float(cost + addition)
            yTop = yTop + 1
        # print E[0:len(E)]


        addition = sys.maxsize
        while list2[yTop][1] == list2[yTop - 1][1]:
            if yTop <= yBottom:
                # print vertexList[list1[yTop][2]-1]
                if vertexList[list2[yTop][2]] == 0:
                    vertexList[list2[yTop][2]] = 1
                    newV = list2[yTop]
                    # print list1[yTop][2]
                    s = len(E)
                    i = 0
                    while (i <= s - 1):
                        d1 = calc_distance(newV, E[i])
                        d2 = calc_distance(newV, E[i + 1])

                        lenEdge = calc_distance(E[i], E[i + 1])
                        newAddition = d1 + d2 - lenEdge
                        if newAddition < addition:
                            addition = newAddition
                            v1 = E[i]
                            v2 = E[i + 1]
                            #			print ("additon: %d" %addition)
                            #			print "\n"
                            #			print newV
                            #			print v1
                            #			print v2

                            idx = i + 1
                        i = i + 2

                    # print "\n"
                    #		print "SIX"
                    #		print newV
                    #		print v1
                    #		print v2


                    E.append((E[idx]))
                    E[idx] = newV
                    E.append((newV))
                    cost = float(cost + addition)
                yTop = yTop + 1
            # print E[0:len(E)]

        addition = sys.maxsize
        # while list1[yBottom][1]==list1[yBottom-1][1]:
        if yBottom >= yTop:
            # print vertexList[list1[yBottom][2]-1]
            if vertexList[list2[yBottom][2]] == 0:
                vertexList[list2[yBottom][2]] = 1
                newV = list2[yBottom]
                # print list1[yBottom][2]
                s = len(E)
                i = 0
                while i <= s - 1:
                    d1 = calc_distance(newV, E[i])
                    d2 = calc_distance(newV, E[i + 1])

                    lenEdge = calc_distance(E[i], E[i + 1])
                    newAddition = d1 + d2 - lenEdge
                    #		     print ("newAddition4: %d" %newAddition)
                    if newAddition < addition:
                        addition = newAddition
                        v1 = E[i]
                        v2 = E[i + 1]
                        #			print ("additon: %d" %addition)
                        #			print "\n"
                        #			print newV
                        #			print v1
                        #			print v2

                        idx = i + 1
                    i = i + 2
                #
                #		print "\n"
                #		print "SEVEN"
                #		print newV
                #		print v1
                #		print v2


                E.append((E[idx]))
                E[idx] = newV
                E.append((newV))
                cost = float(cost + addition)
            yBottom = yBottom - 1
        # print E[0:len(E)]


        addition = sys.maxsize
        while list2[yBottom][1] == list2[yBottom + 1][1]:
            if yBottom >= yTop:
                # print vertexList[list1[yBottom][2]-1]
                if vertexList[list2[yBottom][2]] == 0:
                    vertexList[list2[yBottom][2]] = 1
                    newV = list2[yBottom]
                    # print list1[yBottom][2]
                    s = len(E)
                    i = 0
                    while i <= s - 1:
                        d1 = calc_distance(newV, E[i])
                        d2 = calc_distance(newV, E[i + 1])
                        lenEdge = calc_distance(E[i], E[i + 1])
                        newAddition = d1 + d2 - lenEdge
                        if newAddition < addition:
                            addition = newAddition
                            v1 = E[i]
                            v2 = E[i + 1]
                            #			print ("additon: %d" %addition)
                            #			print "\n"
                            #			print newV
                            #			print v1
                            #			print v2

                            idx = i + 1
                        i = i + 2
                    # print "\n"
                    #		print "EIGHT"
                    #		print newV
                    #		print v1
                    #		print v2


                    E.append((E[idx]))
                    E[idx] = newV
                    E.append((newV))
                    cost = float(cost + addition)
                yBottom = yBottom - 1
            # print E[0:len(E)]
    # return cost

    m = [[0] * (2) for x in range(size)]
    i = 0
    while i < (len(E) - 1):
        if m[E[i][2]][0] == 0:
            m[E[i][2]][0] = E[i + 1][2]
        else:
            m[E[i][2]][1] = E[i + 1][2]
        if m[E[i + 1][2]][0] == 0:
            m[E[i + 1][2]][0] = E[i][2]
        else:
            m[E[i + 1][2]][1] = E[i][2]
        i = i + 2

    i = m[0][0]
    q = 0
    path = []
    k = 1
    #     while (k!=m[0][1]):
    while k != 0:
        if (m[i][0] == q):
            q = i
            i = m[i][1]
            path.append(q)
        # return q
        else:
            q = i
            i = m[i][0]
            path.append(q)
        # return q
        k = q
    return cost, path


# print len(m)
#     print ("\n")
#     print E[0:len(E)]
#     print ("Length of E: %d" %len(E))
#     print ("\n")
#     print m[0:len(m)]

def writeFile(name, contents, method='a'):
    try:
        f = open(name, method)
    except:
        print("The file could not be opened: ", sys.exc_info()[0])

    f.write(contents)
    f.write('\n')
    f.close()


if __name__ == "__main__":
	(ifile, ofile) = cmd_line_io(sys.argv[1:])

	if (ifile  != '') & (ofile != ''):
		print ('Running...')

		z = read_file(ifile)

		start = time.time()
		distance, path = algorithm(z)
		stop = time.time()
		duration = stop - start

		pathstring = ''
		count = 0
		for i in range(0,len(path)):
			pathstring += str(path[i]) +'\n'
			count= count+1

		resultsummary = 'FILE: %s  had points %i; Distance: %d; Time: %d \n'%(ifile, count, distance, duration)

		writeFile(ofile, str(distance), method='a')
		writeFile(ofile, str(pathstring), method='a')
		writeFile('resultsumary.txt', resultsummary, method='a')



	elif(ifile  == '') & (ofile == ''):
		print ('This will now cycle though all files we have')

		filenames = ['tsp_example_1.txt', 'tsp_example_2.txt','test-input-1.txt', 'test-input-2.txt',
             'test-input-3.txt', 'test-input-4.txt', 'test-input-5.txt', 'test-input-6.txt', 'test-input-7.txt','tsp_example_3.txt']

		#for i in range(0, len(filenames)):
		for i in range(0, len(filenames)):
			curFile = filenames[i]
			input = 'tsp_test_cases/' + curFile
			output = 'tsp_results/' + curFile

			z = read_file(input)
			result = []

			start = time.time()
			distance, path = algorithm(z)
			stop = time.time()
			duration = stop - start

			pathstring = ''
			count = 0
			for i in range(0,len(path)):
				pathstring += str(path[i]) +'\n'
				count= count+1

			resultsummary = 'FILE: %s  had points %i; Distance: %d; Time: %f \n'%(curFile, count, distance, duration)

			writeFile(output, str(distance), method='a')
			writeFile(output, str(pathstring), method='a')
			writeFile('tsp_results/resultsumary.txt', resultsummary, method='a')

	else:
		print ('Incorrect parameters provided try p4 -h')
