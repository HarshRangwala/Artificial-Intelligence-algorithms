'''
graph = {'A': set(['B', 'C', 'E']),
         'B': set(['A','D', 'E']),
         'C': set(['A', 'F', 'G']),
         'D': set(['B']),
         'E': set(['A', 'B','D']),
         'F': set(['C']),
         'G': set(['C'])}
'''
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, st, v = None):
    if v is None:
        v = set()
        print("V",v)
    v.add(st)
    print("V after adding",v)
    for next in graph[st]-v:
        #print("NEXT",next)
        #print("DIFFERENCE PART",graph[st]-v)
        dfs(graph, next, v)
        #print("GRAPH",graph,"\t NEXT",next,"\t V",v)
    return v
dfs(graph, 'C')

def paths(graph, st, goal, path=None):
    #print("GRAPH: \T    ST \t   ST\t GOAL\t path",graph,st,goal,path)
    if path is None:
        path = [st]
        #print("PATH",path)
        #print("ST",st)
    if st == goal:
        return path
    for next in graph[st] - set(path):
        return paths(graph, next, goal, path+[next])
list(paths(graph, 'A','F'))
