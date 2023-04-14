N = int(input())
food = map(int, input().split())

ans = 0
a = 0
b = 0
c = 0
for k in food:
    aa = abs(k - a)
    ab = abs(10 - (k - a))
    ba = abs(k - b)
    bb = abs(10 - (k - b))
    ca = abs(k - c)
    cb = abs(10 - (k - c))
    L = [aa, ab, ba, bb, ca, cb]
    if min(L) == aa:
        ans += aa
        a = k
    elif min(L) == ab:
        ans += ab
        a = k
    elif min(L) == ba:
        ans += ba
        b = k
    elif min(L) == bb:
        ans += bb
        b = k
    elif min(L) == ca:
        ans += ca
        c = k
    elif min(L) == cb:
        ans += cb
        c = k
    #print(a, b, c)
print(ans)