# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments_sorted_by_end = sorted(segments, key = lambda x:x[1])
    current_endpoint = segments_sorted_by_end[0][1]
    points.append(current_endpoint)
    
    for i in segments_sorted_by_end:
        if segments_sorted_by_end[i][0] > current_endpoint:
            points.append(segments_sorted_by_end[i][1])
            current_endpoint = segments_sorted_by_end[i][1]
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
