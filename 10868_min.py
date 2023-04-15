import sys

def init_tree(node, start, end):
    if (start == end):
        tree[node] = nums[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = min(init_tree(node * 2, start, mid), init_tree(node * 2 + 1, mid + 1, end))
        return tree[node]

def min_tree(node, start, end, left, right):
    if (end < left or right < start):
        return 1E13
    if (left <= start and end <= right):
        return tree[node]
    mid = (start + end) // 2
    return min(min_tree(node * 2, start, mid, left, right) , min_tree(node*2 +1, mid + 1, end, left, right))


nums = []
tree = []

if __name__ == "__main__":
    N, M = map(int, input().split())
    # nums = [0] * N
    
    # init
    for i in range(N):
        nums.append(int(sys.stdin.readline()))
    
    # tree
    tmp = 1
    while tmp < 2 * N:
        tmp *= 2
    tree = [0] * (tmp + 1)
    
    init_tree(1, 0, N-1)
    
    ans = ""
    for i in range(M):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        ak = min_tree(1, 0, N-1, a-1, b-1)
        print(ak) # 이게 더 빠르다?!
    #     ans += str(ak) + "\n"
    
    # print(ans)
    