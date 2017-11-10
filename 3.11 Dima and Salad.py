n,k=3,2
a=[0]*(n+1)
b=[0]*(n+1)
sa=raw_input().split(' ')
sb=raw_input().split(' ')
bmax=10000
M=2*bmax+1
bag=[-1]*M
for i in range(1,n+1):
    a[i]=int(sa[i-1])
    b[i]=int(sb[i-1])*k-a[i]
bag[bmax]=0
for i in range(1,n+1):
    if b[i]<=0:
        for j in range(M):
            if bag[j]!=-1:
                if j+b[i]>=0 and j+b[i]<M:
                    bag[j+b[i]]=max(bag[j+b[i]],bag[j]+a[i])
    else:
        for j in range(M-1,0,-1):
            if bag[j]!=-1:
                if j+b[i]>=0 and j+b[i]<M:
                    bag[j+b[i]]=max(bag[j+b[i]],bag[j]+a[i])
print bag[bmax]


