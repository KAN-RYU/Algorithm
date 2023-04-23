from collections import deque
import sys

def bfs(limit):
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    q = deque()
    q.append(start)
    
    while q:
        now = q.popleft()
        if now == end:
            return True
        for weight, dest in graph[now]:
            if visited[dest] != 0 or weight < limit:
                continue
            q.append(dest)
            visited[dest] = 1
    return False

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((c,b))
        graph[b].append((c,a))
        
    # for i in range(1, n+1):
    #     graph[i].sort(reverse=True)
    
    start, end = map(int, sys.stdin.readline().split())
    
    low, high = 1, int(1E9)
    while low <= high:
        mid = (low + high) // 2
        if bfs(mid):
            low = mid + 1
        else:
            high = mid - 1
    
    print(high)
