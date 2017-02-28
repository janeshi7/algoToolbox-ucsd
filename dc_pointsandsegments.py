# Uses python3
import sys
from collections import defaultdict

def fast_count_segments(starts, ends, points):
    if n != len(starts) or n!= len(ends) or m != len(points):
        return []
    if m == 0 or n == 0:
        return []
    if len(starts) != len(ends):
        return []
    
    cnt = [0] * len(points)
    count = 0

    all_in_list = [(x, "l") for x in starts]
    all_in_list += [(x, "p") for x in points]
    all_in_list += [(x, "r") for x in ends]
    
    all_in_list.sort()
    
    for value, kind in all_in_list:
        if kind == "l":
            count += 1
        elif kind == "r":
            count -= 1
        elif kind == "p":
            cnt[p_store[value][0]] = count
            p_store[value].remove(p_store[value][0])
                   
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #print (n, m, starts, ends, points)

    #creat a dictionary containing points and their index, compensate space for time 
    p_store = defaultdict(list)
    j = 0
    for i in points:
        p_store[i].append(j)
        j += 1

    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')



