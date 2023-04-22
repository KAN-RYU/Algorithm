import sys

# R=0 G=1 B=2
dp = []
rgb = []

def dp_update():
    N = len(rgb)
    ans = 1E10
    for i in range(N):
        dp.append([0]*3)
    for first_color in range(3): # fix first house's color
        for i in range(3):
            if i == first_color:
                dp[0][i] = rgb[0][i]
            else:
                dp[0][i] = 1E10
        for i in range(1, N):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]
            
        for i in range(3):
            if i == first_color:
                continue
            ans = min(ans, dp[N-1][i])
        # print(ans)
    
    return ans
    
    

if __name__ == "__main__":
    N = int(input())
    
    for i in range(N):
        rgb.append(list(map(int, sys.stdin.readline().split())))
    
    print(dp_update())