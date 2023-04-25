import sys
from copy import deepcopy

def move(board, direction):
    dirList = [(0,1),(0,-1),(1,0),(-1,0)]
    end = 0 if min(dirList[direction]) == -1 else N-1
    start = N-1 if min(dirList[direction]) == -1 else 0
    
    if direction < 2:
        for i in range(N):
            tmp = 0
            borderT = end
            for j in range(end - dirList[direction][1], start - dirList[direction][1], -dirList[direction][1]):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][borderT] == 0:
                        board[i][borderT] = tmp
                    elif board[i][borderT] == tmp:
                        board[i][borderT] = tmp * 2
                        borderT -= dirList[direction][1]
                    else:
                        borderT -= dirList[direction][1]
                        board[i][borderT] = tmp
    else:
        for j in range(N):
            tmp = 0
            borderT = end
            for i in range(end - dirList[direction][0], start - dirList[direction][0], -dirList[direction][0]):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[borderT][j] == 0:
                        board[borderT][j] = tmp
                    elif board[borderT][j]== tmp:
                        board[borderT][j] = tmp * 2
                        borderT -= dirList[direction][0]
                    else:
                        borderT -= dirList[direction][0]
                        board[borderT][j] = tmp

    # for c in board:
    #     print(*c)
    # print(direction,'\n')
    return board

def dfs(board, cnt) -> int:
    ans = 0
    if cnt == 5:
        # for c in board:
        #     print(*c)
        # print()
        for i in range(N):
            ans = max(ans, max(board[i]))
        return ans
    
    for i in range(4):
        tmp_board = move(deepcopy(board), i)
        ans = max(ans, dfs(tmp_board, cnt + 1))
    return ans


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    board = []
    for _ in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    
    ans = dfs(board, 0)
    print(ans)