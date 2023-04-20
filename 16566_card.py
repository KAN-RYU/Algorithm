import sys

N, M, K = 0, 0, 0
card = []
minsu = []
unionL = []

def union(idx, next_idx):
    if next_idx >= M:
        return
    aidx = find(idx)
    anext_idx = find(next_idx)
    unionL[aidx] = anext_idx

def find(x):
    if x == unionL[x]:
        return x
    
    tmp = find(unionL[x])
    unionL[x] = tmp
    return tmp

# binary search upperbound
def binary_search_upperbound(x):
    start, end = 0, M
    while start < end:
        mid = (start + end) // 2
        if card[mid] > x:
            end = mid
        else:
            start = mid + 1
    return end

if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().split())
    card = [int(x) for x in sys.stdin.readline().split()]
    minsu = [int(x) for x in sys.stdin.readline().split()]
    unionL = [x for x in range(M)]
    card.sort()
    
    for ms in minsu:
        idx = binary_search_upperbound(ms)
        aidx = find(idx)
        print(card[aidx])
        union(aidx, aidx+1)
        # print(*unionL)