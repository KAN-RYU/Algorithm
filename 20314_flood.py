import sys

max_tree = []
h = []
t = []

def init_tree(node, start, end):
    if (start == end):
        max_tree[node] = h[start]
        return max_tree[node]
    else:
        mid = (start + end) // 2
        max_tree[node] = max(init_tree(node * 2, start, mid), init_tree(node * 2 + 1, mid + 1, end))
        return max_tree[node]

def max_height(node, start, end, left, right):
    if (end < left or right < start):
        return -1
    if (left <= start and end <= right):
        return max_tree[node]
    mid = (start + end) // 2
    return max(max_height(node * 2, start, mid, left, right) , max_height(node*2 +1, mid + 1, end, left, right))

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    h = [0]
    h.extend([int(x) for x in sys.stdin.readline().split()])
    t = [0,0]
    t.extend([int(x) for x in sys.stdin.readline().split()])
    left_max = [0] * (N + 1)
    right_max = [0] * (N + 1)
    
    # tree
    tmp = 1
    while tmp < 2 * N:
        tmp *= 2
    max_tree = [0] * (tmp + 1)
    
    init_tree(1, 1, N)
    
    # to left max
    p = N
    i = N
    s = 0
    while i > 0:
        # p<--- (i)
        # init from new point when cannot go left
        if i < p:
            p = i
            s = 0
        # time < height
        while 1 < p and s + t[p] <= h[p-1]:
            s += t[p]
            p -= 1
        left_max[i] = max_height(1, 1, N, p, i)
        s -= t[i]
        i -= 1
        
    # to right max
    p = 1
    i = 1
    s = 0
    while i < N:
        # (i) --->p
        # init form new point when cannot go right
        if p < i:
            p = i
            s = 0
        # time < height
        while p < N and s + t[p+1] <= h[p+1]:
            p += 1
            s += t[p]
        right_max[i] = max_height(1, 1, N, i, p)
        s -= t[i+1]
        i += 1
    # print(*left_max)
    # print(*right_max)
    k = []
    for i in range(1, N+1):
        k.append(max(left_max[i], right_max[i]))
    print(*k)