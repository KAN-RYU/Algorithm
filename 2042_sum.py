def init_tree(nums, tree, node, start, end):
    if (start == end):
        tree[node] = nums[start]
        return tree[node]
    else:
        tree[node] = init_tree(nums, tree, node * 2, start, (start + end) // 2) + init_tree(nums, tree, node * 2 + 1, (start+end) // 2 + 1, end)
        return tree[node]

def sum_tree(tree, node, start, end, left, right):
    if (left > end or right < start):
        return 0
    if (left <= start and end <= right):
        return tree[node]
    return sum_tree(tree, node * 2, start, (start+end)//2, left, right) + sum_tree(tree, node*2 +1, (start+end) //2 + 1, end, left, right)

def update_tree(tree, node, start, end, index, diff):
    if (index < start or end < index):
        return
    tree[node] = tree[node] + diff
    if start != end:
        update_tree(tree, node*2, start, (start+end)//2, index, diff)
        update_tree(tree, node*2+1, (start+end)//2+1, end, index, diff)
        
if __name__ == "__main__":
    N, M, K = map(int, input().split())
    
    nums = []
    
    # init
    for i in range(N):
        nums.append(int(input()))
    
    # tree
    tmp = 1
    while True:
        if tmp >= 2**N:
            break
        tmp *= 2
    tree = [0] * (tmp + 1)
    
    init_tree(nums, tree, 1, 0, N-1)
    
    
    for i in range(M+K):
        a, b, c = map(int, input().split())
        if a == 1:
            update_tree(tree, 1, 0, N-1, b-1, c - nums[b-1])
            # lf = 1
            # for i in range(1, len(tree)-2):
            #     print(tree[i], end= " ")
            #     if i == lf:
            #         print()
            #         lf = lf *2 +1
        elif a == 2:
            print(sum_tree(tree, 1, 0, N-1, b-1, c-1))
    