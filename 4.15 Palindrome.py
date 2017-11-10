s=raw_input()
l=len(s)
dp=[[0]*(l+1) for _ in range(l+1)]
letter=[['']*(l+1) for _ in range(l+1)]
for i in range(1,l+1):
    dp[i][i]=1

    letter[i][i]=s[i-1]
for i in range(1,l):
    for j in range(1,l-i+1):
        p=i+j
        if s[i-1]==s[j-1]:
            dp[i][j]=dp[i+1][j-1]+1
            letter[i][j]+=letter[i+1][j-1]
