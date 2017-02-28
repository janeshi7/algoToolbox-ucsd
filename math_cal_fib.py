#Use python2

def cal_fib(n):
    if n <= 1:
        return n
    else:
        lst =[0,1]
        for i in range(2,n+1):
            lst.append(lst[i-1]+lst[i-2])
        return lst[n]

print(cal_fib(int(raw_input())))