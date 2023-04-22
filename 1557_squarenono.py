import sys

KMAX = 1e9
NMAX = 2e9
MAX = 50000
K = 0
sign = [0] * MAX
sp = [0] * MAX
primes = []

def build_prime():
    for i in range(2, MAX):
        if sp[i] == 0:
            primes.append(i)
        for j in primes:
            if i*j > MAX-1:
                break
            sp[i*j] = j
            if i%j == 0:
                break

# if prime squared return -1
# otherwise return number of primes
def is_prime_square(n: int) -> int:
    pre = -1
    cnt = 1
    if n == 1: return 2
    while sp[n] > 0:
        if sp[n] == pre:
            return -1
        pre = sp[n]
        n //= sp[n]
        cnt += 1
    if pre == n:
        return -1
    return cnt

def compute_sign():
    for i in range(1, MAX):
        numofprime = is_prime_square(i)
        if numofprime == -1:
            sign[i] = 0
        elif numofprime % 2 == 0: # plus when prime number is even
            sign[i] = 1
        else:
            sign[i] = -1

# compute number of squarenono less than n
def Q(n: int) -> int:
    result = 0
    i = 1
    while i*i <= n:
        result += sign[i] * (n // (i*i))
        i += 1
    # print(result)
    return result

if __name__ == "__main__":
    K = int(input())
    
    build_prime()
    compute_sign()
    
    # print(*sign[:20])
    start = 1
    end = K * 2
    ans = end
    while start <= end:
        mid = (start + end)//2
        if Q(mid) < K:
            start = mid + 1
        else:
            end = mid - 1
            ans = mid
    print(ans)