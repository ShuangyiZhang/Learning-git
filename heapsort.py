from heapq import heappop,heappush,heapify
def heapsort(alist):
    h=[]
    for value in alist:
        heappush(h,value)
    return [heappop(alist) for i in range(len(alist))]
a=[1,5,3,2,5,7,8,6,4,3,9]
print heapsort(a)