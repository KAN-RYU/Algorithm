import sys

dp = []
num = []
s = []
e = []

def dp_update(N):
    for i in range(1, N+1):
        dp[i][i] = 1
    for i in range(1, N):
        if num[i] == num[i+1]:
            dp[i][i+1] = 1
    for i in range(N, 0, -1):
        for j in range(i+2, N + 1):
            if dp[i+1][j-1] != 0 and num[i] == num[j]:
                dp[i][j] = 1

if __name__ == "__main__":
    N = int(input())
    num = [0]
    num.extend(list(map(int, sys.stdin.readline().split())))
    M = int(input())
    for i in range(M):
        a,b = map(int, sys.stdin.readline().split())
        s.append(a)
        e.append(b)
    
    for i in range(N+1):
        dp.append([0] * (N+1))
    dp_update(N)
    
    # for i in range(N+1):
    #     print(*dp[i])
    
    for i in range(M):
        print(dp[s[i]][e[i]])