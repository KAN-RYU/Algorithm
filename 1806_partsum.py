import sys

if __name__ == "__main__":
    N, S = map(int, sys.stdin.readline().split())
    num = list(map(int,sys.stdin.readline().split()))
    left = 0
    right = 1
    ans = 1e6
    partsum = num[0]
    while left <= right:
        if partsum < S:
            if N <= right: # indexerror 조심
                break
            partsum += num[right]
            right += 1
        else:
            ans = min(ans, right-left)
            partsum -= num[left]
            left += 1
        # print(partsum, ans)
    if ans >= 1e6:
        ans = 0
    print(ans)