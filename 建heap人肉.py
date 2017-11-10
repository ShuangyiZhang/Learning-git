def heap(alist):
    l=len(alist)-1
    for i in range(l/2,-1,-1):
        move(alist,i,l)

def move(alist,first,last):
    smallest=2*first+1
    while smallest<=last:
        if smallest<last and alist[smallest]>alist[smallest+1]:
            smallest+=1
        if alist[smallest]<alist[first]:
            alist[smallest],alist[first]=alist[first],alist[smallest]
            first=smallest
            smallest=2*first+1
        else:
            return
a=[1,3,5,7,9,2,4,6,8,10]
heap(a)
print a