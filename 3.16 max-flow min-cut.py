MAXN=220
INF=10**9
cap=[[0]*MAXN for _ in range(MAXN)]
dad=[0]*MAXN
n,m=int(raw_input().split())
def bfs(s,t):
    for i in range(n+1):
        dad[i]=-1
    q=[]
    dad[s]=s
    q.append(s)
    while q:
        x=q.pop(0)
        if x==t:return True
        for i in range(n+1):
            if cap[x][i]>0 and dad[i]==-1:
                dad[i]=x
                q.append(i)
    return False
for i in range(m):
    a,b,c=map(int,raw_input().split(' '))
    cap[a][b]=c
ans=0
while bfs(1,n):
    f=INF
    x=n
    while x!=1:
        f=min(f,cap[dad[x]][x])
        x=dad[x]
    x=n
    while x!=1:
        cap[dad[x]][x]-=f
        cap[x][dad[x]]+=f
        x=dad[x]
    ans+=f
print ans