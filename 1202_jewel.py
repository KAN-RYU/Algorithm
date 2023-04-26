import heapq
import sys

# 각 가방에 들어갈 수 있는 보석 중 가장 가치가 높은 보석을 넣는다
# 무게 제한이 낮은 가방부터 채우면 OK

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    MV = []
    for _ in range(N):
        mt, vt = map(int, sys.stdin.readline().split())
        MV.append((mt, vt))
    
    C = []
    for _ in range(K):
        C.append(int(sys.stdin.readline()))
    
    MV.sort()
    C.sort()
    
    pq_max = []
    idx = 0
    ans = 0 
    for i in range(K):
        while idx < N and MV[idx][0] <= C[i]:
            heapq.heappush(pq_max, (-MV[idx][1]))
            idx += 1
        if len(pq_max) > 0:
            ans += -heapq.heappop(pq_max)
    print(ans)