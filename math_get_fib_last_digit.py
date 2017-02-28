#Use python2

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n
    else:
        lst =[0,1]
        for i in range(2,n+1):
            lst.append((lst[i-1] + lst[i-2]) % 10)
        return lst[n]

print get_fibonacci_last_digit(int(raw_input()))