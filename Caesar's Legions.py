#n1,n2,k1,k2=map(int,raw_input().split())
def permutation(m1,m2,last):
    sum = 0
    if last==0:
        if m1 == 0: return 0
        if m1==1:
            if m2<=k2:
                return 1
            else:
                return 0
        l=min(k1,m1)
        for i in range(1,l+1):
            sum+= permutation(m1-i,m2,1)
        return sum
    else:
        if m2 == 0: return 0
        if m2==1:
            if m1<=k1:
                return 1
            else:return 0
        l=min(k2,m2)
        for i in range(1,l+1):
            sum+= permutation(m1,m2-i,0)
        return sum
global n1,n2,k1,k2
n1,n2,k1,k2=10,10,5,5
print permutation(n1,n2,1)+permutation(n1,n2,0)