import sys
import math

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

x, y, z = read_file('sample.txt')
#print x[0:len(x)]
#print y[0:len(y)]
#print z[0:len(z)]

def calc_distance(p1, p2):
    xdis = abs(p1[0] - p2[0])
    ydis = abs(p1[1] - p2[1])

    # dat hypotenuse - 3 figures
    #dis = "%.3f" % math.sqrt(math.pow(xdis, 2) + math.pow(ydis, 2))
    dis = int( math.sqrt(math.pow(xdis, 2) + math.pow(ydis, 2)))

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
    #looks over the list swapping if the ys are larger
#    for i in range(0,len(a)-1):
#        if (a[i][v] == a[i+1][v]) & (a[i][l] > a[i+1][l]):
            #swap
#            f,g = a[i], a[i+1]
#	    print a[i]
#            a[i], a[i+1]= g,f
#	    print a[i]

#    return a

#newZ = []
#newZ = sort_coordinates (z, 0)
#print newZ[0:len(newZ)]
#print newZ[1][3]

def algorithm (l):
     size=len(l)
     list1=sort_coordinates(l,0)
     list2=sort_coordinates(l,1)
     xTop=0
     xBottom=size-1
     yTop=0
     yBottom=size-1
     
     vertexList=[0]*size

     #find the left most vertex(vertices). Connect if more than one
     smallXsmallY=list1[xTop]
     if (vertexList[list1[xTop][2]]==0):
	vertexList[list1[xTop][2]]=1
    
     E = []
     
     while (list1[xTop][0]==list1[xTop+1][0]):
	E.append((int(list1[xTop][0]), int(list1[xTop][1]), int(list1[xTop][2])))
	E.append((int(list1[xTop+1][0]), int(list1[xTop+1][1]), int(list1[xTop+1][2])))
        if (vertexList[list1[xTop][2]]==0):
		vertexList[list1[xTop][2]]=1 
	if (vertexList[list1[xTop+1][2]]==0):
		vertexList[list1[xTop+1][2]]=1
	xTop=xTop+1
	
     smallXlargeY=list1[xTop]
     if (vertexList[list1[xTop][2]]==0):
	vertexList[list1[xTop][2]]=1

     #find the top most vertex(ices). Connect if more than one
     largeYlargeX=list2[yBottom]    
     if (vertexList[list2[yBottom][2]]==0):
	vertexList[list2[yBottom][2]]=1

     while (list2[yBottom][1]==list2[yBottom-1][1]):
	E.append((int(list2[yBottom][0]), int(list2[yBottom][1]), int(list2[yBottom][2])))
	E.append((int(list2[yBottom-1][0]), int(list2[yBottom-1][1]), int(list2[yBottom-1][2])))
        if (vertexList[list2[yBottom][2]]==0):
		vertexList[list2[yBottom][2]]=1
	if (vertexList[list2[yBottom-1][2]]==0):
		vertexList[list2[yBottom-1][2]]=1
	yBottom=yBottom-1
    
#     if (yBottom==size-1):
#	yBottom=yBottom-1
#     yBottom=yBottom+1 
     largeYsmallX=list2[yBottom]
#     largeYsmallX=list2[yBottom+1]
    
     if (vertexList[list2[yBottom][2]]==0):
	vertexList[list2[yBottom][2]]=1
     
#     yBottom=yBottom+1

     #connect left most vertex (if more than one, 
     #top vertex of left most vertices) WITH top more vertex
     #(if more than one, left vertex of top most vertices) 
     #unless it turns out to be the same vertex
     if (smallXlargeY!=largeYsmallX):
	E.append((smallXlargeY))
     	E.append((largeYsmallX))



     largeXlargeY=list1[xBottom]    
     if (vertexList[list1[xBottom][2]]==0):
	vertexList[list1[xBottom][2]]=1

     while (list1[xBottom][0]==list1[xBottom-1][0]):
	E.append((int(list1[xBottom][0]), int(list1[xBottom][1]), int(list1[xBottom][2])))
	E.append((int(list1[xBottom-1][0]), int(list1[xBottom-1][1]), int(list1[xBottom-1][2])))
	if (vertexList[list1[xBottom][2]]==0):
		vertexList[list1[xBottom][2]]=1
	if (vertexList[list1[xBottom-1][2]]==0):
		vertexList[list1[xBottom-1][2]]=1
	
	xBottom=xBottom-1


     largeXsmallY=list1[xBottom]

     if (largeXlargeY!=largeYlargeX):
	E.append((largeYlargeX))

     	E.append((largeXlargeY))



     smallYsmallX=list2[yTop]
    
     while (list2[yTop][1]==list2[yTop+1][1]):
	E.append((int(list2[yTop][0]), int(list2[yTop][1]), int(list2[yTop][2])))
	E.append((int(list2[yTop+1][0]), int(list2[yTop+1][1]), int(list2[yTop+1][2])))

	if (vertexList[list2[yTop][2]]==0):
		vertexList[list2[yTop][2]]=1
	if (vertexList[list2[yTop+1][2]]==0):
		vertexList[list2[yTop+1][2]]=1
	yTop=yTop+1
	
     smallYlargeX=list2[yTop]
     if (vertexList[list2[yTop][2]]==0):
	vertexList[list2[yTop][2]]=1


     if (largeXsmallY!=smallYlargeX):
	E.append((largeXsmallY))

     	E.append((smallYlargeX))

     if (smallYsmallX!=smallXsmallY):
	E.append((smallYsmallX))
     	E.append((smallXsmallY))
     cost=0
     i=0
     while i <(len(E)-1):
        length = calc_distance(E[i],E[i+1])
  # 	print E[i][2]
  # 	print E[i+1][2]
	cost=cost+length
#	print ("cost: %d" %cost)
        i=i+2
     
#     print E[0:len(E)]
     xTop=xTop+1
     xBottom=xBottom-1
     yTop=yTop+1
     yBottom=yBottom-1
    
     for i in range (0, size):
        addition = sys.maxsize
        if xTop<=xBottom:
	     #print vertexList[list1[xTop][2]-1]
	     if vertexList[list1[xTop][2]]==0:
	     	vertexList[list1[xTop][2]]=1
	     	newV=list1[xTop]
		#print list1[xTop][2]
		s=len(E)
		i=0
		while (i<=s-1):
		     d1= calc_distance(newV, E[i])
		     d2 = calc_distance(newV,E[i+1])
		     lenEdge = calc_distance(E[i],E[i+1])
		     newAddition = d1+d2-lenEdge
		     if newAddition<addition:
			addition=newAddition
			v1=E[i]
			v2=E[i+1]
		#	print ("additon: %d" %addition)
		#	print newV
		#	print v1
		#	print v2
			idx=i+1
		     i=i+2
		E.append((v2))
		E[idx]=newV
		E.append((newV))
		cost=cost+addition
	     xTop=xTop+1	
	     	
	addition=sys.maxsize
	while list1[xTop][0]==list1[xTop-1][0]:
	  if xTop<=xBottom:
	     #print vertexList[list1[xTop][2]-1]
	     if vertexList[list1[xTop][2]]==0:
	     	vertexList[list1[xTop][2]]=1
	     	newV=list1[xTop]
		#print list1[xTop][2]
		s=len(E)
		i=0
		while (i<=s-1):
		     d1= calc_distance(newV, E[i])
		     d2 = calc_distance(newV,E[i+1])
		     lenEdge = calc_distance(E[i],E[i+1])
		     newAddition = d1+d2-lenEdge
		     if newAddition<addition:
			addition=newAddition
			v1=E[i]
			v2=E[i+1]
#			print ("additon: %d" %addition)
#			print newV
#			print v1
#			print v2

			idx=i+1
		     i=i+2
		E.append((v2))
		E[idx]=newV
		E.append((newV))
		cost=cost+addition
	     xTop=xTop+1	
	


        addition = sys.maxsize
	#m=list1[xBottom][0]
	#n=list1[xBottom-1][0]
	#while list1[xBottom][0]==list1[xBottom-1][0]:
        if xBottom>=xTop:
	     #print xBottom
	     #print xTop
	     #print vertexList[list1[xBottom][2]-1]
	     if vertexList[list1[xBottom][2]]==0:
	     	vertexList[list1[xBottom][2]]=1
	     	newV=list1[xBottom]
		#print list1[xBottom][2]
		s=len(E)
		i=0
		while (i<=s-1):
		     d1= calc_distance(newV, E[i])
		     d2 = calc_distance(newV,E[i+1])

		     lenEdge = calc_distance(E[i],E[i+1])
		     newAddition = d1+d2-lenEdge
		     if newAddition<addition:
			addition=newAddition
			v1=E[i]
			v2=E[i+1]
#			print ("additon: %d" %addition)
#			print newV
#			print v1
#			print v2

			idx=i+1
		     i=i+2
		E.append((v2))
		E[idx]=newV
		E.append((newV))
		cost=cost+addition
	     xBottom=xBottom-1
	
	while list1[xBottom][0]==list1[xBottom+1][0]:
          if xBottom>=xTop:
	     if vertexList[list1[xBottom][2]]==0:
	     	vertexList[list1[xBottom][2]]=1
	     	newV=list1[xBottom]
		#print list1[xBottom][2]
		s=len(E)
		i=0
		while (i<=s-1):
		     d1= calc_distance(newV, E[i])
		     d2 = calc_distance(newV,E[i+1])

		     lenEdge = calc_distance(E[i],E[i+1])
		     newAddition = d1+d2-lenEdge
		     if newAddition<addition:
			addition=newAddition
			v1=E[i]
			v2=E[i+1]
#			print ("additon: %d" %addition)
#			print newV
#			print v1
#			print v2

			idx=i+1
		     i=i+2
		E.append((v2))
		E[idx]=newV
		E.append((newV))
		cost=cost+addition
	     xBottom=xBottom-1	



        addition=sys.maxsize
        #while list1[yTop][1]==list1[yTop+1][1]:
        if yTop<=yBottom:
	     #print vertexList[list1[yTop][2]-1]
	     if vertexList[list2[yTop][2]]==0:
	     	vertexList[list2[yTop][2]]=1
	     	newV=list2[yTop]
		#print list1[yTop][2]
		s=len(E)
		i=0
		while (i<=s-1):
		     d1= calc_distance(newV, E[i])
		     d2 = calc_distance(newV,E[i+1])
		     lenEdge = calc_distance(E[i],E[i+1])
		     newAddition = d1+d2-lenEdge
		     if newAddition<addition:
			addition=newAddition

			v1=E[i]
			v2=E[i+1]
#			print ("additon: %d" %addition)
#			print newV
#			print v1
#			print v2

			idx=i+1
		     i=i+2
		E.append((v2))
		E[idx]=newV
		E.append((newV))
		cost=cost+addition
	     yTop=yTop+1
	
	addition=sys.maxsize
        while list2[yTop][1]==list2[yTop-1][1]:
         if yTop<=yBottom:
	     #print vertexList[list1[yTop][2]-1]
	     if vertexList[list2[yTop][2]]==0:
	     	vertexList[list2[yTop][2]]=1
	     	newV=list2[yTop]
		#print list1[yTop][2]
		s=len(E)
		i=0
		while (i<=s-1):
		     d1= calc_distance(newV, E[i])
		     d2 = calc_distance(newV,E[i+1])

		     lenEdge = calc_distance(E[i],E[i+1])
		     newAddition = d1+d2-lenEdge
		     if newAddition<addition:
			addition=newAddition
			v1=E[i]
			v2=E[i+1]
#			print ("additon: %d" %addition)
#			print newV
#			print v1
#			print v2

			idx=i+1
		     i=i+2
		E.append((v2))
		E[idx]=newV
		E.append((newV))
		cost=cost+addition
	     yTop=yTop+1	



        addition = sys.maxsize
        #while list1[yBottom][1]==list1[yBottom-1][1]:
        if yBottom>=yTop:
	     #print vertexList[list1[yBottom][2]-1]
	     if vertexList[list2[yBottom][2]]==0:
	     	vertexList[list2[yBottom][2]]=1
	     	newV=list2[yBottom]
		#print list1[yBottom][2]
		s=len(E)
		i=0
		while i<=s-1:
		     d1= calc_distance(newV, E[i])
		     d2 = calc_distance(newV,E[i+1])

		     lenEdge = calc_distance(E[i],E[i+1])
		     newAddition = d1+d2-lenEdge
#		     print ("newAddition4: %d" %newAddition)
		     if newAddition<addition:
			addition=newAddition
			v1=E[i]
			v2=E[i+1]
#			print ("additon: %d" %addition)
#			print newV
#			print v1
#			print v2

			idx=i+1
		     i=i+2
		E.append((v2))
		E[idx]=newV
		E.append((newV))
		cost=cost+addition
	     yBottom=yBottom-1
	
	addition=sys.maxsize
	while list2[yBottom][1]==list2[yBottom+1][1]:
          if yBottom>=yTop:
	     #print vertexList[list1[yBottom][2]-1]
	     if vertexList[list2[yBottom][2]]==0:
	     	vertexList[list2[yBottom][2]]=1
	     	newV=list2[yBottom]
		#print list1[yBottom][2]
		s=len(E)
		i=0
		while i<=s-1:
		     d1= calc_distance(newV, E[i])
		     d2 = calc_distance(newV,E[i+1])
		     lenEdge = calc_distance(E[i],E[i+1])
		     newAddition = d1+d2-lenEdge
		     if newAddition<addition:
			addition=newAddition
			v1=E[i]
			v2=E[i+1]
#			print ("additon: %d" %addition)
#			print newV
#			print v1
#			print v2

			idx=i+1
		     i=i+2
		E.append((v2))
		E[idx]=newV
		E.append((newV))
		cost=cost+addition
	     yBottom=yBottom-1	
     print  cost
    
     m=[[0]*(2) for x in xrange(size)]
     i=0
     while i<(len(E)-1):
	if m[E[i][2]][0]==0:
	     m[E[i][2]][0]=E[i+1][2]
	else:
	     m[E[i][2]][1]=E[i+1][2]     
	if m[E[i+1][2]][0]==0:
	     m[E[i+1][2]][0]=E[i][2]
	else:
	     m[E[i+1][2]][1]=E[i][2]
	i=i+2

     i = m[0][0]
     q=0
     k=1
#     while (k!=m[0][1]):
     while k!=0:
	if (m[i][0]==q):
	     q=i
	     i=m[i][1]
	     print q
	else:
	     q=i
	     i=m[i][0]
	     print (q)
	k=q
     print len(m)     
#     print ("\n")
#     print E[0:len(E)]
#     print ("Length of E: %d" %len(E))
#     print ("\n")
#     print m[0:len(m)]
algorithm(z)
