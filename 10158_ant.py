import sys

if __name__ == "__main__":
    w, h = map(int, sys.stdin.readline().split())
    p, q = map(int, sys.stdin.readline().split())
    t = int(sys.stdin.readline())
    
    dx = t % (2 * w)
    dy = t % (2 * h)
    
    lx = p + dx
    ly = q + dy
    
    lx = w - (lx % w) if lx // w == 1 else lx % w
    ly = h - (ly % h) if ly // h == 1 else ly % h
    
    print(f"{lx} {ly}")