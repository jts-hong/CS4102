
def insertionSort(list, i, j):
	for a in range(i,j+1):
		key = list[a]
		b=a-1
		while b>=0 and key<list[b]:
			list[b+1]=list[b]
			b-=1
		list[b+1] = key


def partition(list, i, j):
	pivot = list[j]
	x = i - 1
	for a in range(i, j):
		if (list[a] <= pivot):
			x+= 1
			list[x],list[a]= list[a],list[x]
	list[x + 1],list[j]=list[j],list[x + 1]
	return x+1

def quickSort(list, i, j, minSize):
	if (i < j):
		if minSize>1 and (j-i+1)<=minSize:
			insertionSort(list,i,j)
		else:
			pi = partition(list, i,j)
			quickSort(list, i, pi - 1,minSize)
			quickSort(list, pi + 1, j,minSize)
"""
def printArray(arr, size):
     
    for i in range(size):
        print(arr[i], end = " ")
    print()
 

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1,1)
ano = [10, 7, 8, 9, 1, 5]
insertionSort(ano,0,n-1)
print("Sorted array:")
printArray(ano, n)
printArray(arr, n)
"""