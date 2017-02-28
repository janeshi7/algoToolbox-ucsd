# Uses python3
import sys
import random

def partition3(a, l, r):
    
    x = a[l]
    i = l
    j = l
    k = r
    
    while i <= k:
        if a[i] < x:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
            #print ("less than", a, "i =", i, "j = ", j, "k= ", k)
        elif a[i] > x:
            a[i], a[k] = a[k], a[i]
            k -= 1
            #print ("greater than", a, "i =", i, "j = ", j, "k = ", k)
        elif a[i] == x:
            i += 1
            #print ("equal", a, "i =", i, "j = ", j, "k = ", k)
    #print ("two indeces", j, k)
    #print ("partitioned array", a)
    return j, k
            
            
        
def randomized_quick_sort(a, l, r):
    if l >= r:
        #print ("cool")
        return
    
    while l < r:
        #print ("hot")
        k = random.randint(l, r)
        #print (k)
        a[l], a[k] = a[k], a[l]
        #print (a)
        (m1, m2) = partition3(a, l, r)
        if (m1 - l) < (r - m2):
            #print ("woops")
            randomized_quick_sort(a, l, m1-1)
            l = m2 + 1
            
        else:
            #print ("m2+1 = ", m2+ 1, "r = ", r)
            randomized_quick_sort(a, m2 + 1, r)
            r = m1 - 1          

#data = list(map(int, raw_input().split()))
#n = data[0]
#a = data[1:]
#randomized_quick_sort(a, 0, n - 1)
#for x in a:
    #print x

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')