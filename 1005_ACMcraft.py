import sys
from collections import deque

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, K = map(int, sys.stdin.readline().split())
        Dtime = [0]
        Dtime.extend(list(map(int,sys.stdin.readline().split())))
        pre = [0] * (N+1)
        suc = []
        for _ in range(N+1):
            suc.append(deque())
        for _ in range(K):
            x, y = map(int, sys.stdin.readline().split())
            suc[x].append(y)
            pre[y] += 1
        
        Goal = int(sys.stdin.readline())
        result = [0] * (N+1)
        q = deque()
        for i in range(1, N+1):
            if pre[i] == 0:
                q.append(i)
        
        while pre[Goal] > 0:
            current = q.popleft()
            for next in suc[current]:
                result[next] = max(result[next], result[current] + Dtime[current])
                pre[next] -= 1
                if pre[next] == 0:
                    q.append(next)
        print(result[Goal] + Dtime[Goal])