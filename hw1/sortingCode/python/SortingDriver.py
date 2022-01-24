
from Sorting import insertionSort, quickSort
import copy
import random
import time

def checkSorted(orig, sorted):

	# Make sure size is the same
	if len(orig) != len(sorted):
		print("ERROR...original list and sorted list have different lengths...",end='')
		return False
	
	# Make sure new array is sorted
	for i in range(1,len(sorted)):
		if sorted[i] < sorted[i-1]:
			print("ERROR...the sorted list does not appear to be correctly sorted...",end='')
			return False

	# Make sure the same elements are in each array
	count = {}
	for i in range(len(orig)):
		if orig[i] not in count:
			count[orig[i]] = 1
		else:
			count[orig[i]] = count[orig[i]]+1
		
		if sorted[i] not in count:
			count[sorted[i]] = -1
		else:
			count[sorted[i]] = count[sorted[i]]-1

	for key in count:
		if count[key] != 0:
			print("ERROR...The sorted list does not contain the same elements that the original list does...",end='')
			return False
	
	return True



SIZE = 2000
	
# Make an array (vector) to sort. Fill with random numbers
list = []
for i in range(SIZE):
	list.append((int)(random.randrange(SIZE)))

# Make copies to sort
x1 = copy.deepcopy(list) 
x2 = copy.deepcopy(list)
x3 = copy.deepcopy(list)
x4 = copy.deepcopy(list)
x5 = copy.deepcopy(list)
x6 = copy.deepcopy(list)

def timedif(size,array):
	
	ins = copy.deepcopy(array) 
	qui = copy.deepcopy(array)

	start1 = time.time()

	#print("Sorting using insertion sort...",end='')
	insertionSort(ins, 0, len(ins)-1)
	#print("DONE\nChecking if sorted correctly...",end='')
	checkSorted(list, ins)
	#print("DONE")

	end1 = time.time()
	td1=end1-start1

	start2 = time.time()

	#print("Sorting using quick sort...",end='')
	quickSort(qui, 0, len(qui)-1, 1);
	#print("DONE\nChecking if sorted correctly...",end='')
	checkSorted(list, qui);
	#print("DONE")

	end2 = time.time()
	td2=end2-start2

	print(td1)
	print(td2)
	print(td1-td2)

#timedif(2000)
#timedif(4000)
#timedif(6000)

def make_sort_list(size):
	a_list = []
	for i in range(0,size+1):
		a_list.append(i)
	return a_list
x = make_sort_list(500)


"""
x1 = copy.deepcopy(x)
x2 = copy.deepcopy(x)

print("Sorting using insertion sort...",end='')
start1 = time.time()
insertionSort(x1, 0, len(x)-1)
print("DONE\nChecking if sorted correctly...",end='')

checkSorted(x, x1)
print("DONE")
end1 = time.time()
td1=end1-start1
print(td1)


start2 = time.time()

print("Sorting using quicksort...",end='')
quickSort(x2, 0, len(x)-1,1);
print("DONE\nChecking if sorted correctly...",end='')
checkSorted(x, x2);
print("DONE")
end2 = time.time()
td2=end2-start2

print(td2)



x3 = copy.deepcopy(x)
x4 = copy.deepcopy(x)
x3.sort(reverse=True)
x4.sort(reverse=True)

print("Sorting using insertion sort...",end='')
start1 = time.time()
insertionSort(x3, 0, len(x)-1)
print("DONE\nChecking if sorted correctly...",end='')

checkSorted(x, x3)
print("DONE")
end1 = time.time()
td1=end1-start1
print(td1)


start2 = time.time()

print("Sorting using quicksort...",end='')
quickSort(x4, 0, len(x)-1,1)
print("DONE\nChecking if sorted correctly...",end='')
checkSorted(x, x4)
print("DONE")
end2 = time.time()
td2=end2-start2

print(td2)
"""
"""
for i in range(SIZE):
	a = random.randrange(5,10)
	list.append(SIZE - i+a)

# Make copies to sort
ins = copy.deepcopy(list) 
qui = copy.deepcopy(list)


start1 = time.time()

print("Sorting using insertion sort...",end='')
insertionSort(ins, 0, len(ins)-1)
print("DONE\nChecking if sorted correctly...",end='')
checkSorted(list, ins)
print("DONE")
end1 = time.time()
td1=end1-start1

start2 = time.time()

print("Sorting using quick sort...",end='')
quickSort(qui, 0, len(qui)-1, 10)
print("DONE\nChecking if sorted correctly...",end='')
checkSorted(list, qui)
print("DONE")

end2 = time.time()

td2=end2-start2
print("insertion:",td1)
print("quick:",td2)
print("time differece:")
print(td1-td2)
"""
start1 = time.time()
quickSort(x1, 0, len(x1)-1, 5)
end1 =time.time()
start2 = time.time()
quickSort(x2, 0, len(x2)-1, 10)
end2 =time.time()
start3 = time.time()
quickSort(x3, 0, len(x3)-1, 15)
end3 =time.time()
start4 = time.time()
quickSort(x4, 0, len(x4)-1, 20)
end4 =time.time()
start5 = time.time()
quickSort(x5, 0, len(x5)-1, 30)
end5 =time.time()
start6 = time.time()
quickSort(x6, 0, len(x6)-1, 45)
end6 =time.time()

print("minisize of 5",end1-start1)
print("minisize of 10",end2-start2)
print("minisize of 15",end3-start3)
print("minisize of 20",end4-start4)
print("minisize of 30",end5-start5)
print("minisize of 45",end6-start6)
print("A")
list = []
l2 = []
l3= []
for i in range(500):
	list.append((int)(random.randrange(500)))
for i in range(1000):
	l2.append((int)(random.randrange(1000)))
for i in range(1500):
	l3.append((int)(random.randrange(1500)))
print(timedif(500,list))
print(timedif(1000,l2))
print(timedif(1500,l3))

print(0.001600027084350586-0.03478598594665527)
print(0.002668142318725586-0.0724477767944336)