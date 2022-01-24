class V():
     def __init__(self,n,t,s=None,c_s=False):
          self.n=n
          self.t=t
          self.s=s
          self.c_s=c_s
class DisjSet:
     def __init__(self,v):
          self.v = v
          self.graph=[]
     def findSet(self,parent,i):
          if parent[i.n].n == i.n:
               return parent[i.n]
          return self.findSet(parent,parent[i.n])
     '''
     def union(self,u,v):
          self.link(self.findSet(self.parent,u),self.findSet(self.parent,v))
     
     def union(self,u,v):
          if (u=="b" and v =="j") or (u =="b" and v=="o"):
               self.link(self.findSet(self.parent,u),self.findSet(self.parent,v))
          if (u=="j" and v =="b") or (u =="o" and v=="b"):
               self.link(self.findSet(self.parent,v),self.findSet(self.parent,u))
          if (u=="j" and v =="o") or (u =="j" and v=="j"):
               self.link(self.findSet(self.parent,u),self.findSet(self.parent,v))
          if (u=="o" and v =="j") or (u =="o" and v=="o"):
               self.link(self.findSet(self.parent,u),self.findSet(self.parent,v))

          if u=="b" and v =="s" and self.parent[v]!= "j" and self.parent[v]!="o":
               self.link(self.findSet(self.parent,u),self.findSet(self.parent,v))
          
          if u=="j" and v =="s" and self.parent[v]!= "b" and self.parent[v]!="o":
               self.link(self.findSet(self.parent,u),self.findSet(self.parent,v))

          if u=="o" and v =="s" and self.parent[v]!= "b" and self.parent[v]!="j":
               self.link(self.findSet(self.parent,u),self.findSet(self.parent,v))

          if u=="l" and v =="l" and self.parent[u]!= self.parent[v]:
               self.link(self.findSet(self.parent,u),self.findSet(self.parent,v))

          if u=="s" and v =="l" and self.parent[v]== "s":
               self.link(self.findSet(self.parent,u),self.findSet(self.parent,v))

          if u=="l" and v =="s" and self.parent[u]== "s":
               self.link(self.findSet(self.parent,u),self.findSet(self.parent,v))

     def link(self,u,v):
          if self.rank[u]>self.rank[v]:
               self.parent[v]=u
          else:
               self.parent[u]=v
               if self.rank[u] ==self.rank[v]:
                    self.rank[v] =self.rank[v]+1

     '''



     def union1(self, u, v, dic):
          u_root=self.findSet(dic,u)
          v_root=self.findSet(dic,v)
          if u_root == v_root:return False
          #----for all breaker to box, it will connect----#
          elif u.t == "breaker" and v.t == "box":
               dic[v_root.n] = u_root
               return True
          elif v.t == "breaker" and u.t == "box":
               dic[u_root.n] = v_root
               return True

          #-----for all breaker to switchm, it will connect under the root of breaker-----#
          elif u.t == "breaker" and v.t == "switch":
               if v == v_root:
                    dic[v_root.n] = u_root
                    return True
          elif v.t == "breaker" and u.t == "switch":
               if u == u_root:
                    dic[u_root.n] = v_root
                    return True
          #-----for all box and switch, it will connect under switch if it is the root----#
          elif u.t == "box" and v.t == "switch":
               if v == v_root:
                    dic[v_root.n] = u_root
                    return True
          elif v.t == "box" and u.t == "switch":
               if u == u_root:
                    dic[u_root.n] = v_root
                    return True
          #-----for all box and box it doesn;it doesn't matter which way----#
          if u.t == "box" and v.t == "box":
               if v == v_root:
                    dic[v_root.n] = u_root
                    return True
               elif u_root.t == "breaker":
                    dic[v_root.n] = u_root
                    return True
               elif v_root.t == "breaker":
                    dic[u_root.n] = v_root
                    return True
               dic[u_root.n] = v_root
               return True
          #-----for light and switch, it will connect if they are the same switch-----#
          elif u.t == "switch" and v.t == "light":
               if v.s == u.n and not v.c_s:
                    dic[v_root.n] = u_root
                    v.c_s = True
                    return True
               else:return False
          elif v.t == "switch" and u.t == "light":
               if u.s == v.n and not u.c_s:
                    dic[u_root.n] = v_root
                    u.c_s = True
                    return True
               else:return False
          #-----for lights, will connect if they are the same switch
          if u.t == "light" and v.t == "light":
               if u.s == v.s:
                    if u.c_s and v.c_s:return False
                    if v.c_s:
                         dic[u_root.n] = v_root
                         return True
                    if u.c_s:
                         dic[v_root.n] = u_root
                         return True
                    dic[u_root.n] = v_root
                    return True
               else:return False
          else:return False

#-----Initiate a DisjSet-----#
# eAccepted = 0
# s = DisjSet()


x = input()
a = x.split(" ")
num_node = int(a[0])
num_edge = int(a[1])
vert=[]
#print(num_node,type(num_node))
#print(num_edge,type(num_edge))

#-----Getting Nodes-----#

for i in range(num_node):
     a= input().split(" ")
     n=a[0]
     t=a[1]
     if t == 'outlet':
        t = 'box'
     if t == 'switch':
          switch = n
     v = V(n, t)
     if t == 'light':
          v = V(n, t, switch)
     vert.append(v)

#print(s.parent)
#-----Getting Edges-----#


gra = DisjSet(vert)
for i in range(num_edge):
     a= input().split(" ")
     n1=a[0]
     n2=a[1]
     w=int(a[2])
     for ver in gra.v:
        if ver.n== n1:
            v1=ver
     for ver in gra.v:
          if ver.n==n2:
               v2=ver
     gra.graph.append([v1,v2,w])


#-----Kruskal-----#
result = []
edge = 0
ind = 0
gra.graph = sorted(gra.graph, key=lambda item: item[2])
dic ={}
for v in gra.v:
     dic[v.n] = v
while edge < len(gra.v) - 1:
     v1, v2, w = gra.graph[ind]
     ind +=1
     if gra.union1(v1, v2, dic) :
          result.append([v1.n, v2.n, w])
          edge +=1
re = 0
for i in result:
     re += i[2]     
# print(dic.values(),dic.keys())
# for i in gra.v:
#      print(i.n,i.t,i.s,i.c_s)
print(re)



'''
s.graph = sorted(s.graph, key=lambda item: item[2])
#print(s.graph)
result =[]


#-----Run Kruskall-----#


while(eAccepted<s.num_v-1):
     a = s.graph.pop(0)
     uset = s.findSet(s.parent,a[0])
     #print(uset)
     vset=s.findSet(s.parent,a[1])
     #print(vset)
     if(uset!=vset):
           eAccepted +=1
           result.append(a)
           print(a)
           s.union(uset,vset)



#-----Getting Results-----#

val=0
for i in result:
     val+=i[2]

print(val)
'''