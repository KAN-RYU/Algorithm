import collections
N = int(input())

ans = collections.deque()
ans.append(N)
i = 1
while i < N:
    if i % 2 == 1:
        ans.appendleft(i)
    else:
        ans.append(i)
    i += 1

ans2 = collections.deque()
i = 1
if (N % 2 == 1):
    ans2.append(N)
    N -= 1
while i <= N // 2:
    ans2.append(i)
    ans2.append(N- i + 1)
    i += 1

print("YES")
print(" ".join(map(str, ans)))
print(" ".join(map(str, ans2)))