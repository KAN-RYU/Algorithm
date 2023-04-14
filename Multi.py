KL = [[10],
      [1],
      [2,4,8,6],
      [3,9,7,1],
      [4,6],
      [5],
      [6],
      [7,9,3,1],
      [8,4,2,6],
      [9,1]]

N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    m = len(KL[a % 10])
    print(KL[a % 10][(b-1) % m])
