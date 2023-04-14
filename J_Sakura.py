import heapq

#f = open("./output")

N, M = map(int, input().split())
#N, M = map(int, f.readline().split())
maxSakura = -1
maxDays = []

start = []
end = []
trees = []

a = 0
b = 0
k = "kba"
sj = "sk day"
bFlag = False
while a < N:
    if not bFlag:
        Si, Ei = map(int, input().split())
        # Si, Ei = map(int, f.readline().split())
        trees.append((Si, Ei))
        
        heapq.heappush(start, (-Si, Si))
        heapq.heappush(end, Ei)
    # print(k, b, a)
    # print(start, end)
    ma = start[0][1]
    mi = end[0]
    if ma <= mi:
        if a - b + 1 == maxSakura:
            maxSakura = a - b + 1
            maxDays.append((ma, mi))
            #print(sj, maxSakura, maxDays)
        elif a - b + 1 > maxSakura:
            maxSakura = a - b + 1
            maxDays = [(ma, mi)]
            #print(sj, maxSakura, maxDays)
    else:
        start.remove((-trees[b][0], trees[b][0]))
        heapq.heapify(start)
        # print(start)
        end.remove(trees[b][1])
        heapq.heapify(end)
        b += 1
        bFlag = True
        # if a != b:
        #     heapq.heappush(start, (-trees[b][0], trees[b][0]))
        #     heapq.heappush(end, trees[b][1])
        continue
    
    bFlag = False
    a += 1

ansD = 0
maxDays.sort()
tmpS = maxDays[0][0]
tmpE = maxDays[0][1]
for d in maxDays:
    if d[0] <= tmpE:
        tmpE = max(tmpE, d[1])
    else:
        ansD += tmpE - tmpS + 1
        tmpS = d[0]
        tmpE = d[1]
ansD += tmpE - tmpS + 1
print(maxSakura, ansD)