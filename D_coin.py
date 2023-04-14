
def inputCoin(x, y):
    coinM = []
    for x in range(x):
        tmp = input()
        tmpL = map(lambda x: 0 if x == '.' else 1, tmp)
        coinM.append(list(tmpL))
        
    return coinM

if __name__ == "__main__":
    ar, ac = map(int, input().split())
    a = inputCoin(ar, ac)
    br, bc = map(int, input().split())
    b = inputCoin(br, bc)
    coinCnt = sum(map(lambda x: x.count(1), a))
    ans = coinCnt
    i = 0
    #print(ar, ac,  br, bc)
    while i < ar + br - 1:
        j = 0
        while j < ac + bc - 1:
            kstart = max(0, i - ar + 1)
            k = kstart
            klimit = min(i, br-1)
            llimit = min(j, bc-1)
            lstart = max(0, j - ac + 1)
            tmpCnt = 0
            #print(i, j, kstart, lstart, klimit, llimit)
            aistart = max(ar - i - 1, 0)
            ajstart = max(ac - j - 1, 0)
            while k <= klimit:
                l = lstart
                while l <= llimit:
                    if (b[k][l] == 1 and b[k][l] == a[aistart + k-kstart][ajstart + l-lstart]):
                        tmpCnt += 1
                    l += 1
                k += 1
            j += 1
            #print(tmpCnt)
            ans = min(ans, coinCnt - tmpCnt)
        i += 1
    print(ans)