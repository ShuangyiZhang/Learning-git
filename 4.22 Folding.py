maxn=105
best=[[0]*maxn for _ in range(maxn)]
mn=[[0]*maxn for _ in range(maxn)]
p=[[0]*maxn for _ in range(maxn)]
s=raw_input()
def canfold(l,r,len):
    for i in range(l,r-len+1):
        if s[i]!=s[i+len]:return False
    return True
def digit(x):
    ans=0
    while x:
        x/=10
        ans+=1
    return ans
def fold(l,r):
    if l>r:return 0
    if not best[l][r]:
        len=r-l+1
        best[l][r]=len
        mn[l][r]=len
        p[l][r]=-1
        for i in range(1,n/2+1):
            if len%i==0:
                if canfold(l,r,i):
                    cand=digit(len/i)+2+fold(l,l+i-1)
                    if cand<best[l][r]:
                        best[l][r]=cand
                        mn[l][r]=i
        for i in range(l,r):
            cand=fold(l,i)+fold(i+1,r)
            if cand<best[l][r]:
                best[l][r]=cand
                p[l][r]=i
    return best[l][r]
def Print(l,r):
    if l>r:return
    len=r-l+1
    if len==best[l][r]:
        for i in range(l,r+1):
            print s[i],
    elif p[l][r]<0:
        print str(len/mn[l][r])+'(',
        Print(l,l+mn[l][r]-1)
        print ')',
    else:
        Print(l,p[l][r])
        Print(p[l][r]+1,r)
#s=raw_input()
n=len(s)
fold(0,n-1)
Print(0,n-1)



