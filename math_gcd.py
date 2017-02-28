#Use python2
def gcd(a,b):
    if b == 0:
        return a
    else:
        adot = a%b
        return gcd(b,adot)
        
a,b = map(int,raw_input().split())
print(gcd(a,b))