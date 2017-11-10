n,m=map(int,raw_input().split())
par=[[i for i in range(n+1)] for _ in range(100)]
ans=[0]*100
def f(c,x):
    if par[c][x]==x:return x
    par[c][x]=f(c,par[c][x])
    return par[c][x]
def union(c,a,b):
    par[c][f(c,a)]=f(c,b)
for i in range(1,m+1):
    a,b,c=map(int,raw_input().split())
    union(c,a,b)
k=int(raw_input())
for i in range(1,k+1):
    a,b=map(int,raw_input().split())
    ans[i]=sum(1 if f(color,a)==f(color,b) else 0 for color in range(1,m+1))
for i in range(1,k+1):
    print ans[i]