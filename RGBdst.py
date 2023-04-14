N = int(input())
L = [0, 0, 0]

for i in range(N):
    R, G, B = map(int, input().split())
    Rs = R + min(L[1], L[2])
    Gs = G + min(L[0], L[2])
    Bs = B + min(L[0], L[1])
    L[0] = Rs
    L[1] = Gs
    L[2] = Bs
    # print(Rs, Gs, Bs)

print(min(Rs, Gs, Bs))