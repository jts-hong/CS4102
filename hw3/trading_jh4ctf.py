import math
import copy
import random
import time

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def helper(strip, size, n):
    min = n
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y - strip[i].y) < min:
            min = math.sqrt((strip[i].x - strip[j].x)*(strip[i].x - strip[j].x)+(strip[i].y - strip[j].y)*(strip[i].y - strip[j].y))
            j += 1
    return min

def rec(P, ori, n):
    if n <= 3:
        min_val = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                if math.sqrt((P[i].x - P[j].x)*(P[i].x - P[j].x)+(P[i].y - P[j].y)*(P[i].y - P[j].y)) < min_val:
                    min_val = math.sqrt((P[i].x - P[j].x)*(P[i].x - P[j].x)+(P[i].y - P[j].y)*(P[i].y - P[j].y))
        return min_val
 
    m = n//2
    mPoint = P[m]
    l = P[:m]
    r = P[m:]
    dl = rec(l, ori, m)
    dr = rec(r, ori, n - m)
    d = min(dl, dr)
    stripP = []
    stripQ = []
    lr = l + r
    for i in range(n):
        if abs(lr[i].x - mPoint.x) < d:
            stripP.append(lr[i])
        if abs(ori[i].x - mPoint.x) < d:
            stripQ.append(ori[i])
 
    stripP.sort(key = lambda point: point.y)
    min_a = min(d, helper(stripP, len(stripP), d))
    min_b = min(d, helper(stripQ, len(stripQ), d))
    return min(min_a,min_b)

def result(P, n):
    P.sort(key = lambda point: point.x)
    ori= copy.deepcopy(P)
    ori.sort(key = lambda point: point.y)   
    return rec(P, ori, n)

'''
filename = "/Users/skg/Desktop/4102/hw3/test.txt"
P =[]
with open(filename) as f:
    b = f.readline()
    #print(b)
    n = int(b[0])
    #print(n)
    for line in f:
        a=line.split(' ')
        if len(a)==1:
            if int(a[0])>0:
                r=result(P,n)
                if r >10000:
                    print("infinity")
                else:
                    print(round(r,4))
                n = int(a[0])
                P.clear()
            else:
                r=result(P,n)
                if r >10000:
                    print("infinity")
                else:
                    print(round(r,4))
                P.clear()
        if len(a)>1:
            #print(float(a[0]),float(a[1]))
            P.append(Point(float(a[0]),float(a[1])))

'''
'''
P =[]
x = input()
while (x!=0):
    a=x.split(' ')
    if len(a)==1:
        if int(a[0])>0:
            r=result(P,n)
            if r >10000:
                print("infinity")
            else:
                result =round(r,4)
                dist = format(result, '.4f')
                print(dist)
            n = int(a[0])
            P.clear()
    if len(a)>1:
        #print(float(a[0]),float(a[1]))
        P.append(Point(float(a[0]),float(a[1])))
    x = input()
result =round(r,4)
dist = format(result, '.4f')
print(dist)

'''
n = input()
while n!=0:
    pointlist = []
    for i in range(n):
        x, y = map(float, input().split())
        p = Point(x, y)
        pointlist.append(p)
    print(result(pointlist))
    n = int(input())


'''
con = True
P=[]
line = input()
b=line.split(' ')
n = int(b[0])
while(con):
    line = input()
    a=line.split(' ')
    if len(a)==1:
        if int(a[0])>0:
            r=result(P,n)
            if r >10000:
                print("infinity")
            else:
                result =round(r,4)
                dist = format(result, '.4f')
                print(dist)
            n = int(a[0])
            P.clear()
        else:
            r=result(P,n)
            if r >10000:
                print("infinity")
            else:
                result =round(r,4)
                dist = format(result, '.4f')
                print(dist)
            P.clear()
            break
    if len(a)>1:
        #print(float(a[0]),float(a[1]))
        P.append(Point(float(a[0]),float(a[1])))

#----________________----#
#----First Experiment----#
#----^^^^^^^^^^^^^^^^----#


def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) *(p1.x - p2.x) +(p1.y - p2.y) *(p1.y - p2.y))
 
#--Size of 100--#
print("Size of 100:\n")
te1 = []
for x in range(100):
    a = round(random.uniform(-5000, 5000), 4)
    b = round(random.uniform(-5000, 5000), 4)
    #print(a,b)
    te1.append(Point(a,b))
te2 = copy.deepcopy(te1)

#Brute-Force:

t1 = time.time()
for i in te1:
    min_val = float('inf')
    for i in range(len(te1)):
        for j in range(i + 1, len(te1)):
            if dist(te1[i],te1[j]) < min_val:
                min_val = dist(te1[i],te1[j])
print(min_val)
t2 = time.time()
print("time for Brute-Force:",t2-t1,)

#Algo:

t3 = time.time()
print(result(te2,len(te2)))
t4 = time.time()
print("time for Algo:",t4-t3,"\n")

#--Size of 200--#
print("Size of 200:\n")
te3 = []
for x in range(200):
    a = round(random.uniform(-5000, 5000), 4)
    b = round(random.uniform(-5000, 5000), 4)
    #print(a,b)
    te3.append(Point(a,b))
te4 = copy.deepcopy(te3)


#Brute-Force:
t1 = time.time()
for i in te3:
    min_val = float('inf')
    for i in range(len(te3)):
        for j in range(i + 1, len(te3)):
            if dist(te3[i],te3[j]) < min_val:
                min_val = dist(te3[i],te3[j])
print(min_val)
t2 = time.time()
print("time for Brute-Force:",t2-t1)

#Algo:
t3 = time.time()
print(result(te4,len(te4)))
t4 = time.time()
print("time for Algo:",t4-t3,"\n")

#--Size of 300--#
print("Size of 300:\n")
te5 = []
for x in range(300):
    a = round(random.uniform(-5000, 5000), 4)
    b = round(random.uniform(-5000, 5000), 4)
    #print(a,b)
    te5.append(Point(a,b))
te6 = copy.deepcopy(te5)


#Brute-Force:
t1 = time.time()
for i in te5:
    min_val = float('inf')
    for i in range(len(te5)):
        for j in range(i + 1, len(te5)):
            if dist(te5[i],te5[j]) < min_val:
                min_val = dist(te5[i],te5[j])
print(min_val)
t2 = time.time()
print("time for Brute-Force:",t2-t1)

#Algo:
t3 = time.time()
print(result(te6,len(te6)))
t4 = time.time()
print("time for Algo:",t4-t3,"\n")
'''