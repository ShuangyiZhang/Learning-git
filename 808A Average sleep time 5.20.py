n,k=map(int,raw_input().split())
a=raw_input().split()
s=0
if n+1>=2*k:
  for i in range(1,n+1):
      t=int(a[i-1])

      if i>=k and i<=n-k+1:
         s+=t*k
      elif i<k:
         s+=t*i
      else:
         s+=t*(n+1-i)
else:
    for i in range(1, n + 1):
        t = int(a[i - 1])

        if i <= k and i >= n - k + 1:
            s += t * (n-k+1)
        elif i <n- k+1:
            s += t * i
        else:
            s += t * (n + 1 - i)
print "%.10f"%(s/(n-k+1.0))
