n = int(input())
x = 0
y = 0

for i in range(n):
    k = input()
    if k == 'D':
        x += 1
    elif k == 'P':
        y += 1
    if x - y >= 2 or y - x >= 2:
        break

print(str(x) + ':' + str(y))