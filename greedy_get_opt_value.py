# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    if capacity == 0:
        return 0
    else:
        max_unit = 0
        capacity_left = capacity 
        tot_value = 0
        unit_value = []
        
        for i in range(n):
            unit_value.append(float(values[i])/weights[i])
        for k in range(n):
            max_unit_value = max(unit_value)
            item = unit_value.index(max_unit_value)
            
            tot_value += max_unit_value * min(weights[item], capacity_left)
            capacity_left -= min(weights[item], capacity_left)
            
            unit_value.remove(max_unit_value)
            values.remove(values[item])
            weights.remove(weights[item])
            
            if capacity_left == 0:
                break
        return tot_value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))

