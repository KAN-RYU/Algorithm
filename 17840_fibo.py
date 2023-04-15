import sys

Q, M = input().split()
Q = int(Q)
M = int(M)

fibo = [0, 1, 1]
while True:
    fibo.append((fibo[-1] + fibo[-2]) % M)
    if (fibo[-1] == 1) and (fibo[-2] == 1):
        break
fibo.pop(0)
fibo.pop()
fibo.pop()

# print(fibo)

newfibo = []
for c in fibo:
    tmp = []
    while True:
        tmp.append(c % 10)
        if c < 10:
            tmp.reverse()
            newfibo.extend(tmp)
            break
        c = c // 10

# print(newfibo)

l = len(newfibo)
ans = ""
for i in range(Q):
    N = int(sys.stdin.readline())
    ans += str(newfibo[(N-1)%l]) + "\n"
    
print(ans)
        