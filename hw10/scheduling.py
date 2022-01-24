def BFS(graph, s, t, parent):
    visited = [False] * len(graph)
    q = []
    q.append(s)
    visited[s] = True
 
    while q:
        u = q.pop(0)
        for ind in range(len(graph[u])):
            if visited[ind] is False and graph[u][ind] > 0:
                q.append(ind)
                visited[ind] = True
                parent[ind] = u
 
    if visited[t]:
        return True
    else:
        return False
 
 
def FordFulkerson(graph, source, sink):
    helper= [-1] * (len(graph))
    m=result = 0
    while BFS(graph, source, sink, helper):
        path_flow = float("Inf")
        s = sink
 
        while s != source:
            path_flow = min(path_flow, graph[helper[s]][s])
            s = helper[s]
 
        result += path_flow
        v = sink
 
        while v != source:
            u = helper[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = helper[v]
    return result


a= input().split(" ")
while int(a[0])!=0:
    r = int(a[0])
    c = int(a[1])
    n = int(a[2])
    edge={}
    cla=[]
    for i in range(r):
        a= input().split(" ")
        if a[0] not in edge.keys():
            edge[a[0]]=[a[1]]
        else:
            edge[a[0]].append(a[1])
    for i in range(c):
        a= input().split(" ")
        cla.append([a[0],a[1]])
    # print(edge,cla)


    graph = [[0 for x in range(len(edge.keys())+len(cla)+2)] for x in range(len(edge.keys())+len(cla)+2)]
    # print(cla)

    for i in range(len(edge.keys())):
        graph[0][i+1]=n

    for i in range(len(cla)):
        graph[i+1+len(edge.keys())][-1]=int(cla[i][-1])
    i=1
    for student in edge.keys():
        for c in edge[student]:
            ind =0

            for x in cla:
                if x[0] == c:
                    ind = cla.index(x)

            graph[i][1+ind+len(edge.keys())]=1
        i+=1
    # print(" /n") 
    # for i in graph:
    #     print (i)


    source =0
    sink =1+len(edge.keys())+len(cla)
    #print(sink)

    x=FordFulkerson(graph, source, sink)

    #print(x)
    limit=n*len(edge.keys())
    if x==limit:
        print("Yes")
    else:
        print("No")
    a=input()
    a=input().split(" ")
