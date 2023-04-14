import math
s = input()
u = 0
d = 0
p = 0
c = 0

for ch in s:
    if ch == 'U' or ch == 'C':
        u += 1
        c += 1
    elif ch == 'D' or ch == 'P':
        d += 1
        p += 1

anss = ""
if u > math.ceil(d / 2):
    anss += 'U'
if d > 0:
    anss += 'D'
if p > 0:
    anss += 'P'

print(anss)