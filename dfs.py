graph={
    'A':['B','E'],
    'B':['A','C','D','E'],
    'C':['B','D'],
    'D':['B','C','E'],
    'E':['A','B','D']}
def bfs(node,graph):
    q=[]
    vis=[]
    q.append(node)
    vis.append(node)
    while len(q)!=0:
        p=q.pop(0)
        l=graph[p]
        for i in l:
            if i not in vis:
                q.append(i)
                vis.append(i)
    return vis
def dfs(node,graph,vis=[]):
    if len(vis)==0:
        vis.append(node)
    for i in graph[node]:
        if i not in vis:
            vis.append(i)
            dfs(i,graph,vis)
    return vis
   
n=str(input('enter the input'))
p=bfs(n,graph)
k=dfs(n,graph)
print('the bfs is:',p)
print('the dfs is:',k)

    
    
