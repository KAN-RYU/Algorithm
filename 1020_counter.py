# Idea: ans of YYY...YXXXX == ans of XXXX if ans < X^n - XXXX
# So...

import sys

dp = []
# number of lines for each digits
line_num = [6, 2, 5, 5, 4, 5, 6, 3, 7, 5]

# dp[n][i] == the smallest _n_ digits number with line sum _i_
def dp_update(N: int):
    for nth in range(1, N+1):
        for i in range(2, 8):
            start = (nth - 1) * 2
            end = (nth - 1) * 7 + 1
            for j in range(start, end):
                dp[nth][i + j] = min(dp[nth][i + j], (10**(nth-1)) * dp[1][i] + dp[nth-1][j])
                
def solve(N: int, counter_num: int):
    max_ans = 10 ** N
    answer = max_ans
    unit = counter_num % 10
    # compare 1st digit number
    for i in range(10):
        if (line_num[unit] == line_num[i] and unit != i):
            if i > unit:
                answer = min(answer, i - unit)
            else:
                answer = min(answer, max_ans - (unit - i))
    cnt = line_num[unit] # count current line number
    
    # compare nth digit number
    for nth in range(2, N+1):
        digit = (counter_num % (10 ** nth))
        cnt += line_num[(counter_num // (10 ** (nth-1))) % 10]
        # print("dc", digit, cnt)
        for i in range(10):
            if (cnt - line_num[i]) >= (nth - 1)*2:
                pows = (10 ** (nth-1)) * i
                target = dp[nth - 1][cnt - line_num[i]]
                # print(pows, target)
                if digit != pows + target and target != 1e16:
                    val = pows + target - digit
                    if val <= 0:
                        val += max_ans
                    answer = min(answer, val)
                    # print(answer)
    return answer

if __name__ == "__main__":
    counter = input()
    N = len(counter)
    counter_num = int(counter)
    
    for i in range(N+1):
        dp.append([1e16] * (N*7 + 1))
    
    dp[1][2] = 1
    dp[1][3] = 7
    dp[1][4] = 4
    dp[1][5] = 2
    dp[1][6] = 0
    dp[1][7] = 8
    
    dp_update(N)
    # for l in dp:
    #     print(*l)
    print(solve(N, counter_num))
    