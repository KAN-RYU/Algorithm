N, K = map(int, input().split())

a = []
b = []
c = []

for i in range(N):
    x, y, z = map(int, input().split())
    a.append(x+y)
    b.append(y+z)
    c.append(z+x)

ax = sorted(a, reverse=True)
bx = sorted(b, reverse=True)
cx = sorted(c, reverse=True)
print(max(sum(ax[:K]), sum(bx[:K]), sum(cx[:K])))