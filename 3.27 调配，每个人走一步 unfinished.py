MAXN=10
INF=10**5
cap=[[0]*MAXN for _ in range(MAXN)]
flow=[[0]*MAXN for _ in range(MAXN)]
rank=[-1]*MAXN
n,m=map(int,raw_input().split())
def bfs(s):
    for i in range(2*n+2):
        rank[i]=-1
    rank[s]=0
    q=[]
    q.append(s)
    #print s
    while q:
        x=q.pop(0)
        #print rank
        for i in range(0,2*n+2):
            if cap[x][i]>0 and rank[i]==-1:
                rank[i]=rank[x]+1
                q.append(i)
def dfs(v,f):
    if v==n*2+1: return f
    for i in range(0,2*n+2):
        if rank[i]==rank[v]+1 and cap[v][i]>0:
            d=dfs(i,min(f,cap[v][i]))
            if d>0:
                cap[v][i]-=d
                flow[v][i]+=d
                cap[i][v]+=d
                return d
    return 0
s1=raw_input().split()
s2=raw_input().split()
for i in range(m):
    a,b=map(int,raw_input().split(' '))
    cap[a][b+n]=INF
    cap[b][a+n]=INF
s=0
for i in range(1,n+1):
    cap[0][i]=int(s1[i-1])
    s+=cap[0][i]
    cap[n+i][2*n+1]=int(s2[i-1])
    cap[i][n+i]=INF
#print cap
ans=0
while 1:
    bfs(0)
    #print rank
    if rank[2*n+1]==-1:
        if ans<s:
            print 'NO'
        else:
            print 'YES'
            #print flow
            for i in range(1,n+1):
                for j in range(n+1,2*n+1):
                    print str(flow[i][j]),
                print
        break
    f=1
    #print f
    while f>0:
        f=dfs(0,100)
        #print f
        ans+=f