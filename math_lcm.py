# Uses python2
def gcd(a, b):
    if b == 0:
        return a
    else:
        adot = a % b
        return gcd(b,adot)

def lcm(c, d):
    up = c * d
    down = gcd(c,d)
    return int(up/down)

x,y = map(int,raw_input().split())
print lcm(x,y)