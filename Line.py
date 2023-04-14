N = int(input())

line = []
for i in range(N):
    x, y = map(int, input().split())
    line.append((x,y))

line.sort()
ans = 0
tmpS = -2000000000
tmpE = -2000000000
for d in line:
    if d[0] <= tmpE:
        tmpE = max(tmpE, d[1])
    else:
        ans += tmpE - tmpS
        tmpS = d[0]
        tmpE = d[1]
ans += tmpE - tmpS 
print(ans)