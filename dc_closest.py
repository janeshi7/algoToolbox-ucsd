#Uses python3
import sys
import math 
from collections import defaultdict

def minimum_distance(x, y):
    #write your code here
    min_distance = 0

    if n != len(x) or n != len(y) or len(x) != len(y):
    	return [ ]
    if n < 2:
    	return [ ]

    if len(x) == 2 and len(y) == 2:
    	min_distance = sqrt((x[0] - y[0])^2 + (x[1] + y[1])^2 )
    	return min_distance

    ave = n / 2

    p_left, q_right, min_dist_left = minimum_distance(x[:ave], y[:ave])
    p_right, q_right, min_dist_right = minimum_distance(x[ave:], y[ave:])
    p_merge, q_merge, min_dist_merge = minimum_distance_merge(x, y, min_distance)

    return min(min_dist_merge, min_dist_right, min_dist_left)
    

    return min_distance

#if __name__ == '__main__':
    #input = sys.stdin.read()
    data = list(map(int, input().split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))

	coordinates = defaultdict(list)
	for i in range(n):
    	coordinates[(x[i], y[i])].append(i)
