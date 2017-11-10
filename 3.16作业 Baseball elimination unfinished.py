m=int(raw_input())
INF=1000
n=m*(m-1)/2+1
L=(m-2)*(m-1)/2
MAXN=n+1
cap=[[0]*MAXN for _ in range(MAXN)]
cap_old=[0]*MAXN
flow=[[0]*MAXN for _ in range(MAXN)]
dad=[0]*MAXN
r=[[0]*(m+1) for _ in range(m+1)]
left=[0]*(m+1)
wins=[0]*(m+1)
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
def maxflow(n):
   ans=0
   while bfs(0,n):
       #print dad
       f=INF
       x=n
       while x!=0:
           f=min(f,cap[dad[x]][x])
           x=dad[x]
       x=n
       while x!=0:
           cap[dad[x]][x]-=f
           cap[x][dad[x]]+=f
           flow[dad[x]][x]+=f
           x=dad[x]
       ans+=f
   return ans

def find(i,k):
   if i>k:
       i-=1
   for z1 in range(2, m + 1):
       if z1 == k: continue
       if z1 < k:
           i3 = z1
       else:
           i3 = z1 - 1
       for z2 in range(1, z1):
           if z2 == k: continue
           if z2 < k:
               j3 = z2
           else:
               j3 = z2 - 1
           if flow[(i3 - 2) * (i3 - 1) / 2 + j3][L + i] > 0:
               if z1 not in queue:
                    queue.add(z1)
                    find(z1,k)
               if z2 not in queue:
                    queue.add(z2)
                    find(z2,k)


for i in range(1,m+1):
    wins[i],lose,left[i]=map(int,raw_input().split())
    s=raw_input().split()
    for j in range(1,m+1):
        r[i][j]=int(s[j-1])
#print r
for k in range(1,m+1):
    for i in range(MAXN):
        for j in range(MAXN):
            cap[i][j]=0
            flow[i][j]=0
        cap_old[j] = 0

    #Initialize
    maxf=0
    flag=1
    for i in range(1,m+1):
        if i==k:continue
        if i < k:
            i0 = i
        else:
            i0=i-1
        for j in range(1,i):
            if j==k:continue
            if j<k:
              j0=j
            else:
              j0=j-1
            #print (i0-2)*(i0-1)/2+j0
            cap[0][(i0-2)*(i0-1)/2+j0]=r[i][j]
            cap_old[(i0-1)*(i0-2)/2+j0]=r[i][j]
            maxf+=r[i][j]
            cap[(i0-1)*(i0-2)/2+j0][L+i0]=INF
            cap[(i0-1)*(i0-2)/2+j0][L+j0]=INF
        if wins[k]+left[k]<wins[i]:
            print 'Team '+str(k)+' is mathematically eliminated because '+str(wins[k])+'+'+str(left[k])+'<'+str(wins[i])+' ,so it can never exceed team '+str(i)+' !'
            print
            flag=0
            break
        else:
            cap[L+i0][n]=wins[k]+left[k]-wins[i]
            #cap_old[1][L+i0]=wins[k]+left[k]-wins[i]
    #print cap
    #build graph
    if flag==0:
        continue
    if maxf>maxflow(n):
        #print flow
        #print k
        for p in range(2,m+1):
            if p == k: continue
            if p < k:
                i0 = p
            else:
                i0 = p - 1
            for q in range(1,p):

                if q == k:continue
                if q < k:
                    j0 = q
                else:
                    j0 = q - 1
                num=(i0-2)*(i0-1)/2+j0
                #print num,i0,j0
                if flow[0][num]<cap_old[num]:
                    #print q,p
                    queue = set()
                    queue.add(p)
                    find(p,k)
                    #print queue
                    queue.add(q)
                    find(q,k)
                    s1=0
                    s2=0
                    string = ''
                    #print queue
                    for z1 in queue:
                        s1+=wins[z1]
                        string+=str(z1)+', '
                        for z2 in queue:
                            s2+=r[z1][z2]
                    #print s1+s2/2
        print 'Team ' + str(k) + ' is mathematically eliminated,'
        print 'because team '+string[:(len(string)-2)]+' win a total of '+str(s1+s2/2)+' games.'
        print 'On average, each team wins '+str(s1+s2/2)+'/'+str(len(queue))+' = '+'%.2f'%((s1+s2/2)/float(len(queue)))+' games.'
        print