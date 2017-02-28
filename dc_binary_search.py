# Python 3
import sys

def binary_search(a, x):
    # write your code here
    if len(a) == 0:
        return -1
    if x < a[0] or x > a[-1]:
        return -1
    if x == a[0]:
        return 0
    if x == a[-1]:
        return len(a) - 1

    start, end = 0, len(a) - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        if a[mid] == x:
            return mid
        if a[mid] < x: 
            start = mid
        else: 
            end = mid

    if a[start] == x:
        return start

    if a[end] == x:
        return end
    
    return -1 


if __name__ == '__main__':

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
    	print(binary_search(a, x), end = ' ')