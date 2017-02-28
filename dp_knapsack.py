# Uses python3
#Notice: val = op_weight[i - 1][j - w[i - 1]] + w[i - 1]. Considering the situation when the ith item is used, it is
#necessary to locate the value at this index"[i - 1][j - w[i - 1]]". This locates the optimal weight when both the 
#ith item and its weight are excluded.
import sys

def optimal_weight(W, w):
    if W == 0:
        return 0
    if w == []:
        return 0
    
    n = len(w)
    op_weight = [[0 for i in range(W + 1)] for j in range(n + 1)]
    
    for i in range(1, n + 1): #!!! i here means using the first i items,NOT using i items.
        for j in range(1, W + 1):
            op_weight[i][j] = op_weight[i - 1][j] #Initialize the value as the ith item is not used
            if w[i - 1] <= j:
                val = op_weight[i - 1][j - w[i - 1]] + w[i - 1] #Check the value when the ith item is used
                if val > op_weight[i][j]:
                    op_weight[i][j] = val
                        
    return op_weight[n][W]
    
            
if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
