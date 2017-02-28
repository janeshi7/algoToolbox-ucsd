# Uses python3
import sys
def merge(y, z):
    result = []
    i, j = 0, 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    while i < len(y):
        result.append(y[i])
        i += 1
    while j < len(z):
        result.append(z[j])
        j += 1
    return result

def mergesort(x):
    if len(x) <= 1:
        return x
    else:
        mid = len(x)//2

        left = mergesort(x[:mid])
        right = mergesort(x[mid:])
        return merge(left, right)

def get_majority_element(a, left, right):
    if right != len(a):
        return -1
    
    a_sorted = mergesort(a)
    if right % 2 == 0:
        for i in range(right//2):
            if a_sorted[i] == a_sorted[i + right//2]:
                return 1
        return -1
            
    else:
        for i in range(right//2 + 1):
           # print (i, i+right//2,a_sorted[i],a_sorted[i + right//2] )
            if a_sorted[i] == a_sorted[i + right//2]:
                return 1
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

