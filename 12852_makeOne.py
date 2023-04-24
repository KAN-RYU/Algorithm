import sys

if __name__ == "__main__":
    N = int(input())
    dp = [(1e6,0)] * (N+1)
    dp[1] = (0,0)
    for i in range(1, N):
        j = dp[i][0] + 1 
        if i+1 <= N and j < dp[i+1][0]: # plus 1
            dp[i+1] = (j, i)
        if i*2 <= N and j < dp[i*2][0]: # time 2
            dp[i*2] = (j, i)
        if i*3 <= N and j < dp[i*3][0]: # time 3
            dp[i*3] = (j, i)
    
    k = dp[N][0]
    print(k)
    tmp = N
    while True:
        print(tmp, end=" ")
        tmp = dp[tmp][1]
        if tmp == 0:
            break