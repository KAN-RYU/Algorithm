import sys

def init_tree(nums, tree, node, start, end):
    if (start == end):
        tree[node] = nums[start]
        return tree[node]
    else:
        tree[node] = min(init_tree(nums, tree, node * 2, start, (start + end) // 2), init_tree(nums, tree, node * 2 + 1, (start+end) // 2 + 1, end))
        return tree[node]

def min_tree(tree, node, start, end, left, right):
    if (end < left or right < start):
        return 1E15
    if (left <= start and end <= right):
        return tree[node]
    return min(min_tree(tree, node * 2, start, (start+end)//2, left, right) , min_tree(tree, node*2 +1, (start+end) //2 + 1, end, left, right))
        
if __name__ == "__main__":
    N, M = map(int, input().split())
    
    nums = [0] * N
    
    # init
    for i in range(N):
        nums[i] = int(sys.stdin.readline())
    
    # tree
    tmp = 1
    while True:
        if tmp >= 2*N:
            break
        tmp *= 2
    tree = [0] * (tmp + 1)
    
    init_tree(nums, tree, 1, 0, N-1)
    
    ans = [0] * M
    for i in range(M):
        a, b = map(int, input().split())
        ans[i] = min_tree(tree, 1, 0, N-1, a-1, b-1)
    
    anss = ""
    for c in ans:
        anss += str(c) + "\n"
    
    print(anss)
    