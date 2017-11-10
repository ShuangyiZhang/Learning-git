from heapq import heapify,heappush,heappop
s=raw_input()
k=input()
n=len(s)
a=map(lambda i:(s[i],i),range(n))
heapify(a)
while k and a:
    x,y=heappop(a)
    k-=1
    if k:
        y+=1
        if y<n:heappush(a,(x+s[y],y))
    else:
        print x
        break
else:print 'No such line !'
