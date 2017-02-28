# Uses python2
def cal_fib(n):
    if n <= 1:
        return n
    else:
        lst =[0,1]
        for i in range(2,n+1):
            lst.append(lst[i-1]+lst[i-2])
        return lst[n]

def fmodm(f,m):
    if m == 2:
        period = [0,1,1]
        return period[f%len(period)]
    else:
        modlst = []
        for i in range(50):
            modlst.append(cal_fib(i)%m)
        for j in range(1,51):
            if (modlst[j] == 0) and (modlst[j+1] == 1):
                period1 = modlst[:j]
                break
        return period1[f%len(period1)]
                    
x,y = map(int, raw_input().split())
print fmodm(x,y)