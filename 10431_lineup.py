import sys

if __name__ == "__main__":
    p = int(input())
    for i in range(p):
        case = list(map(int, sys.stdin.readline().split()))
        t = case[0]
        l = case[1:]
        
        sortedL = []
        
        result = 0
        for a in l:
            flag = False
            for j, b in enumerate(sortedL):
                if a < b:
                    result += len(sortedL) - j
                    sortedL.insert(j, a)
                    flag = True
                    break
            if not flag:
                sortedL.append(a)
                continue
        
        print (t, result)