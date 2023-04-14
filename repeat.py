T = int(input())
for i in range(T):
    R, S = input().split()
    R = int(R)
    K = ""
    for c in S:
        K += c * R
    print(K)