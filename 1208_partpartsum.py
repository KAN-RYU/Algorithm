import sys

# 왼쪽 오른쪽 절반씩 합을 구하면서 합의 경우의 수를 dict에
# 따라서 결과값 K*K 비교
subSum = {}
N = 0
S = 0
num = []
cnt = 0

def rightSum(curr, sum_int):
    if curr == N:
        if sum_int in subSum:
            subSum[sum_int] += 1
        else:
            subSum[sum_int] = 1
        return
    
    rightSum(curr+1, sum_int + num[curr])
    rightSum(curr+1, sum_int)

def leftSum(curr, sum_int):
    global cnt
    if curr == N // 2:
        if S-sum_int in subSum:
            cnt += subSum[S-sum_int]
        return
    
    leftSum(curr+1, sum_int + num[curr])
    leftSum(curr+1, sum_int)

if __name__ == "__main__":
    N, S = map(int, sys.stdin.readline().split())
    num = list(map(int, sys.stdin.readline().split()))
    
    rightSum(N//2, 0)
    # print(subSum)
    leftSum(0, 0)

    if S == 0:
        print(cnt-1)
    else:
        print(cnt)