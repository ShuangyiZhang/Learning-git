def heapsort(alist):
    l=len(alist)-1
    for i in range(l/2,-1,-1):
        move(alist,i,l)
    for i in range(l,0,-1):
        if alist[0]>alist[i]:
            alist[0],alist[i]=alist[i],alist[0]
            move(alist,0,i-1)
def move(alist,first,last):
    largest=2*first+1
    while largest<=last:
        if largest<last and alist[largest]<alist[largest+1]:
            largest+=1
        if alist[largest]>alist[first]:
            alist[largest],alist[first]=alist[first],alist[largest]
            first=largest
            largest=2*first+1
        else:
            return
a=[1,3,5,7,9,8,6,4,2,0]
heapsort(a)
print a