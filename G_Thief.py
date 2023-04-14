import collections
N = int(input())

tree = []
for i in range(N+1):
    tree.append([])

for i in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

for i in range(N+1):
    tree[i].sort()

a, b, c = map(int, input().split())

b_map = [99999] * (N+1)
b_bfs = collections.deque()
b_bfs.append((b,0))
b_map[b] = 0
while len(b_bfs) != 0 and b_bfs[0][0] != a:
    currPos = b_bfs.popleft()
    for node in tree[currPos[0]]:
        if b_map[node] == 99999:
            b_map[node] = currPos[1] + 1
            b_bfs.append((node, currPos[1] + 1))

c_map = [99999] * (N+1)
c_bfs = collections.deque()
c_bfs.append((c,0))
c_map[c] = 0
while len(c_bfs) != 0 and c_bfs[0][0] != a:
    currPos = c_bfs.popleft()
    for node in tree[currPos[0]]:
        if c_map[node] == 99999:
            c_map[node] = currPos[1] + 1
            c_bfs.append((node, currPos[1] + 1))


a_map = [99999] * (N+1)
a_bfs = collections.deque()
a_bfs.append((a,0))
a_map[a] = 0
bcatchFlag = True
ccatchFlag = False
escapeFlag = False
while len(a_bfs) != 0:
    currPos = a_bfs.popleft()
    if len(tree[currPos[0]]) == 1:
        escapeFlag = True
        break
    for node in tree[currPos[0]]:
        if a_map[node] == 99999:
            if b_map[node] <= currPos[1] + 1:
                bcatchFlag = True
                continue
            if c_map[node] <= currPos[1] + 1:
                ccatchFlag = True
                continue
            a_map[node] = currPos[1] + 1
            a_bfs.append((node, currPos[1] + 1))
            if len(tree[node]) == 1:
                escapeFlag = True
                break
    if bcatchFlag and ccatchFlag:
        break

if escapeFlag:
    print("YES")
else:
    print("NO")