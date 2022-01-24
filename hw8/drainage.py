import math

def DP(matrix, row, col, last,visited):        
    if row ==-1 or row ==len(matrix):
        return 0    
    if col ==-1 or col ==len(matrix[0]):
        return 0
    if  matrix[row][col] >= last:
        return 0
    if (row,col) in visited.keys():
        return visited[(row,col)]
        
    last = matrix[row][col]
        
    left  = DP(matrix,  row, col - 1, last,visited)
    right = DP(matrix,  row, col + 1, last,visited)
    up    = DP(matrix, row - 1, col,last, visited)
    down  = DP(matrix, row + 1, col,last, visited)

    max_path = max(left,right,up,down)
        
    visited[(row,col)] = max_path + 1
    return 1 + max_path




n = input()
while (True):
    
    for city in range(int(n)):
        name = input()
        name = name.split(" ")
        city_name = name[0]
        row = int(name[1])
        col = int(name[2])
        matrix = [ [ 0 for i in range(row) ] for j in range(col) ]
        for i in range(row):
            put = input()
            put = put.split(" ")
            for j in range(col):
                matrix[i][j]=int(put[j])
        #print(matrix)
        if not matrix or not matrix[0]:
            result = 0
        result = 0
        visited = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                result = max(result, DP(matrix, row, col,10000000, visited))
        print(name[0],":"," ",result)
        
    try:
        n = input()
        if n=='':
            quit()
    except:
        quit()