MAXN=220
INF=10**9
cap=[[0]*MAXN for _ in range(MAXN)]
rank=[-1]*MAXN
n,m=map(int,raw_input().split())
def bfs(s):
    for i in range(n+1):
        rank[i]=-1
    rank[s]=0
    q=[]
    q.append(s)
    while q:
        x=q.pop(0)
        for i in range(1,n+1):
            if cap[x][i]>0 and rank[i]==-1:
                rank[i]=rank[x]+1
                q.append(i)
def dfs(v,f):
    if v==n: return f
    for i in range(1,n+1):
        if rank[i]==rank[v]+1 and cap[v][i]>0:
            d=dfs(i,min(f,cap[v][i]))
            if d>0:
                cap[v][i]-=d
                cap[i][v]+=d
                return d
    return 0
for i in range(m):
    a,b,c=map(int,raw_input().split(' '))
    cap[a][b]=c
ans=0
while 1:
    bfs(1)
    if rank[n]==-1:
        print ans
        break
    f=1
    while f>0:
        f=dfs(1,INF)
        ans+=f
