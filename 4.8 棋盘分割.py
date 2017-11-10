n=3
a=[[0]*9 for _ in range(9)]
f=[[[[[0]*9 for _4 in range(9)] for _3 in range(9)] for _2 in range(9)] for _1 in range(n+1)]
su=0
for i in range(1,9):
    s=raw_input().split()
    for j in range(1,9):
        a[i][j]=int(s[j-1])
        su+=a[i][j]
print su
def F(e,b,c,d):
    total=0
    for i in range(e,c+1):
        for j in range(b,d+1):
           total+=a[i][j]
    return total
for k in range(1,9):
    for l in range(1,9):
        for i in range(1,9):
            for j in range(1,9):
                f[1][k][l][i][j]=F(k,l,i,j)*F(k,l,i,j)
for parts in range(2,n+1):
    for x1 in range(1, 9):
        for y1 in range(1, 9):
            for x2 in range(1, 9):
                for y2 in range(1, 9):
                    a1=1000
                    a2=1000
                    a3=1000
                    a4=1000
                    for p in range(x1 + 1, x2 + 1):
                       if f[parts-1][p][y1][x2][y2]+f[1][x1][y1][p-1][y2]<a1:a1=f[parts-1][p][y1][x2][y2]+f[1][x1][y1][p-1][y2]
                    for p in range(x1, x2):
                       if f[parts-1][x1][y1][p][y2]+f[1][p+1][y1][x2][y2]<a2:a2=f[parts-1][x1][y1][p][y2]+f[1][p+1][y1][x2][y2]
                    for p in range(y1 + 1, y2 + 1):
                       if f[parts-1][x1][p][x2][y2]+f[1][x1][p-1][x2][y2]<a3:a3=f[parts-1][x1][p][x2][y2]+f[1][x1][p-1][x2][y2]
                    for p in range(y1, y2):

                       if f[parts-1][x1][y1][x2][p]+f[1][x1][p+1][x2][y2]<a4:a4=f[parts-1][x1][y1][x2][p]+f[1][x1][p+1][x2][y2]
                    if a1==1000 and a2==1000 and a3==1000 and a4==1000:
                        f[parts][x1][x2][y1][y2]=0
                    else:
                        f[parts][x1][x2][y1][y2]=min(a1,a2,a3,a4)
print f[n][1][1][8][8]-su*su/n


