n=5
blocks=[(6,8,10),(6,10,8),(10,8,6),(5,5,6),(6,5,5)]
graph=[list() for _ in xrange(n)]
for i in range(n):
    for j in range(n):
        if blocks[i][0]<blocks[j][0] and blocks[i][1]<blocks[j][1] or blocks[i][0]<blocks[j][1] and blocks[i][1]<blocks[j][0]:
            graph[i].append((j,blocks[j][2]))
cost=[blocks[i][2] for i in range(n)]
for k in range(n):
    lmax=0
    start=0
    for i in range(n):
        l=len(graph[i])
        if l>lmax:
            lmax=l
            start=i
    for i in range(lmax):
        if cost[graph[start][i][0]]<cost[graph[start][i][1]]+cost[start]:
            cost[graph[start][i][0]]=cost[graph[start][i][1]]+cost[start]
    graph[start]=list()
print max(cost)
