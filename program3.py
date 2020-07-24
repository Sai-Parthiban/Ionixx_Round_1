graph={}
v=int(input("No of Vertex : "))
n=int(input("No of Edges : "))
print("From:\tTo:\tCost:\tDistance:")
a2=[]
for i in range(n):
    a1=[]
    a,b,g,h=map(str,input().split())
    g,h=int(g),int(h)
    if(a not in graph):
        graph[a]=[]
    if(b not in graph):
        graph[b]=[]
    graph[a].append(b)
    graph[b].append(a)
    a1.extend([a,b,int(g),int(h)])
    a2.append(a1)
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
def f(a,b,a2):
    for i in a2:
        if (i[0]==a and i[1]==b) or (i[0]==b and i[1]==a):
           return i[2],i[3]
print("Enter Source and Destination Vertex : ")
s1,s2=map(str,input().split())
r=find_all_paths(graph,s1,s2,path=[])
b2=[]
for i in r:
    cos=0
    dis=0
    b1=[]
    for j in range(len(i)):
        if j!=len(i)-1:
            a,b=f(i[j],i[j+1],a2)
            cos+=a
            dis+=b
    b1.extend([cos,dis,i])
    b2.append(b1)
b2=sorted(b2,key=lambda x:(x[0],x[1]))
s=""
for i in b2[0][2]:
    s+=i+"->"
print("Minimum Path : ",s[:-2])
print("Minimum Cost : ",b2[0][0])
print("Minimum Distance : ",b2[0][1])
    
        
