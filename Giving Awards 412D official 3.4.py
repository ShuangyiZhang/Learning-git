from sys import stdin
from random import shuffle
def main():
    n, m = map(int, stdin.readline().split())
    s = [set() for _ in xrange(n+1)]
    for _ in xrange(m):
        a, b = map(int, stdin.readline().split())
        s[b].add(a)
    a = range(1, n+1)
    shuffle(a)
    for i in xrange(n):
        for j in xrange(i-1, -1, -1):
            if a[j] not in s[a[j+1]]:
                break
            else:
                a[j], a[j+1] = a[j+1], a[j]
    print ' '.join(map(str, a))
main()
