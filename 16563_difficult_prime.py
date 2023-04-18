# Linear sieve prime
import sys

primes = []
sp = []
LIMIT = 5000001

def build_prime():
    for i in range(2, LIMIT):
        if sp[i] == 0:
            primes.append(i)
        for j in primes:
            if i*j > LIMIT-1:
                break
            sp[i*j] = j
            if i%j == 0:
                break

if __name__ == "__main__":
    N = int(input())
    k = list(map(int, sys.stdin.readline().split()))
    sp = [0] * LIMIT
    
    build_prime()
    for ki in k:
        num = ki
        while sp[num] > 1:
            print(f"{sp[num]} ", end="")
            num //= sp[num]
        print(f"{num}")