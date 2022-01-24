class Vertice:
    def __init__(self, name, type, switch=None):
        self.name = name
        self.type = type
        self.switch = switch
        self.connectToSwitch = False


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, v1, v2, weight):
        self.graph.append([v1, v2, weight])

    def makeSet(self, vertices, set):
        for v in vertices:
            set[v.name] = v

    def findRoot(self, v1, set):
        name = v1.name
        if set[v1.name].name == name:
            return set[name]
        return self.findRoot(set[name], set)

    def union(self, v1, v2, set, v1_root, v2_root):
        if v1_root == v2_root:
            return False

        # (breaker-->box)
        elif v1.type == "breaker" and v2.type == "box":
            set[v2_root.name] = v1_root
            return True
        elif v2.type == "breaker" and v1.type == "box":
            set[v1_root.name] = v2_root
            return True

        # # (breaker-->outlet)
        # elif v1.type == "breaker" and v2.type == "outlet":
        #     set[v2_root.name] = v1_root
        #     return True
        # elif v2.type == "breaker" and v1.type == "outlet":
        #     set[v1_root.name] = v2_root
        #     return True

        # (breaker-->switch)
        elif v1.type == "breaker" and v2.type == "switch":
            if v2 == v2_root:
                set[v2_root.name] = v1_root
                return True
        elif v2.type == "breaker" and v1.type == "switch":
            if v1 == v1_root:
                set[v1_root.name] = v2_root
                return True

        # # (outlet,box)
        # elif v1.type == "outlet" and v2.type == "box":
        #     if v2 == v2_root:
        #         set[v2_root.name] = v1_root
        #         return True
        #     elif v1_root.type == "breaker":
        #         set[v2_root.name] = v1_root
        #         return True
        #     elif v2_root.type == "breaker":
        #         set[v1_root.name] = v2_root
        #         return True
        #     set[v1_root.name] = v2_root
        #     return True
        #
        # elif v2.type == "outlet" and v1.type == "box":
        #     if v1 == v1_root:
        #         set[v1_root.name] = v2_root
        #         return True
        #     elif v1_root.type == "breaker":
        #         set[v2_root.name] = v1_root
        #         return True
        #     elif v2_root.type == "breaker":
        #         set[v1_root.name] = v2_root
        #         return True
        #     set[v2_root.name] = v1_root
        #     return True

        # # (outlet-->switch)
        # elif v1.type == "outlet" and v2.type == "switch":
        #     if v2 == v2_root:
        #         set[v2_root.name] = v1_root
        #         return True
        # elif v2.type == "outlet" and v1.type == "switch":
        #     if v1 == v1_root:
        #         set[v1_root.name] = v2_root
        #         return True

        # # (outlet-->outlet)
        # if v1.type == "outlet" and v2.type == "outlet":
        #     if v1 == v1_root:
        #         set[v1_root.name] = v2_root
        #         return True
        #     elif v2 == v2_root:
        #         set[v2_root.name] = v1_root
        #         return True
        #     elif v1_root.type == "breaker":
        #         set[v2_root.name] = v1_root
        #         return True
        #     elif v2_root.type == "breaker":
        #         set[v1_root.name] = v2_root
        #         return True
        #     else:
        #         return False

        # (box-->switch)
        elif v1.type == "box" and v2.type == "switch":
            if v2 == v2_root:
                set[v2_root.name] = v1_root
                return True
        elif v2.type == "box" and v1.type == "switch":
            if v1 == v1_root:
                set[v1_root.name] = v2_root
                return True

        # (box->box)
        if v1.type == "box" and v2.type == "box":
            if v2 == v2_root:
                set[v2_root.name] = v1_root
                return True
            elif v1_root.type == "breaker":
                set[v2_root.name] = v1_root
                return True
            elif v2_root.type == "breaker":
                set[v1_root.name] = v2_root
                return True
            set[v1_root.name] = v2_root
            return True

        # (switch-->light)

        elif v1.type == "switch" and v2.type == "light":
            if v2.switch == v1.name and not v2.connectToSwitch:
                set[v2_root.name] = v1_root
                v2.connectToSwitch = True
                return True
            else:
                return False
        elif v2.type == "switch" and v1.type == "light":
            if v1.switch == v2.name and not v1.connectToSwitch:
                set[v1_root.name] = v2_root
                v1.connectToSwitch = True
                return True
            else:
                return False

        # (light,light)
        if v1.type == "light" and v2.type == "light":
            if v1.switch == v2.switch:
                if v1.connectToSwitch and v2.connectToSwitch:
                    return False
                if v2.connectToSwitch:
                    set[v1_root.name] = v2_root
                    return True
                if v1.connectToSwitch:
                    set[v2_root.name] = v1_root
                    return True
                set[v1_root.name] = v2_root
                return True
            else:
                return False
        else:
            return False

    def Kruskal(self):
        result = []
        e = 0
        i = 0
        if len(self.graph) > 1:
            self.graph = sorted(self.graph, key=lambda item: item[2])
        vertices_set = {}
        self.makeSet(self.V, vertices_set)
        while e < len(self.V) - 1:
            v1, v2, weight = self.graph[i]
            i = i + 1
            v1_root = self.findRoot(v1, vertices_set)
            v2_root = self.findRoot(v2, vertices_set)
            if self.union(v1, v2, vertices_set, v1_root, v2_root):
                result.append([v1.name, v2.name, weight])
                # (len(result))
                e = e + 1
        length = 0
        for u, v, weight in result:
            # print("%s -- %s == %d" % (u, v, weight))
            length += weight
        print(length)


def find_ver(ver_name1, graph):
    for ver in graph.V:
        if ver.name == ver_name1:
            return ver


v, n = map(int, input().split())
vertices = []
switch = ''
for i in range(v):
    name, type = map(str, input().split())
    if type == 'outlet':
        type = 'box'
    if type == 'switch':
        switch = name
    v = Vertice(name, type)
    if type == 'light':
        v = Vertice(name, type, switch)
    vertices.append(v)
g = Graph(vertices)
for i in range(n):
    name1, name2, weight = map(str, input().split())
    weight = int(weight)
    v1 = find_ver(name1, g)
    v2 = find_ver(name2, g)
    g.addEdge(v1, v2, weight)
g.Kruskal()
