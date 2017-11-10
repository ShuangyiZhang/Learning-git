from heapq import heapify,heappop
n,w=map(int,raw_input().split())
s=map(int,raw_input().split())
a=[0]*n
p=[]
for i in range(n):
    w-=(s[i]+1)/2
    a[i]=(s[i]+1)/2
    p.append((-s[i],i))


if w<0:
    print -1
else:
    heapify(p)

    while w>0 :
       cur,pos=heappop(p)
       dif=-cur-a[pos]
       if dif<=w:
           a[pos]=-cur

       else:
           a[pos]+=w
       w-=dif
    for i in range(n):
        print a[i],

