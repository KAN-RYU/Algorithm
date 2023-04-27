import sys
import heapq

if __name__ == "__main__":
    # f = open('./1.in', 'r')
    V, E = map(int, sys.stdin.readline().split())
    # V, E = map(int, f.readline().split())
    graph = []
    for _ in range(V+1):
        graph.append({})
    for _ in range(E):
        a, b, w = map(int, sys.stdin.readline().split())
        # a, b, w = map(int, f.readline().split())
        graph[a][b] = w
        graph[b][a] = w
    
    # MST
    q = []
    visit = [False] * (V+1)
    heapq.heappush(q, (0, 1))
    ans = 0
    while len(q) > 0: # all 느리다. 쓰지말자자
        weightT, current = heapq.heappop(q)
        if visit[current]: # 이렇게 넣어주자
            continue
        ans += weightT
        visit[current] = True
        for key in graph[current].keys():
            if not visit[key]:
                heapq.heappush(q, (graph[current][key], key))
        # print(q)
        
    
    print(ans)
    # print(visit)