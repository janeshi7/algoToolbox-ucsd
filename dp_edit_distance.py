# Uses python3
def edit_distance(s, t):
    n = len(s)
    m = len(t)
    min_distance = [[0 for i in range(m + 1)] for j in range(n + 1)]
    
    #Initialize the values for min_distance[i][0] and min_distance[0][j]
    for i in range(n + 1):
        min_distance[i][0] = i
    for i in range(m + 1):
        min_distance[0][i] = i
    
    #Compute the values for the rest locations
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            insertion = min_distance[i][j - 1] + 1
            deletion = min_distance[i - 1][j] + 1
            match = min_distance[i - 1][j - 1]
            dismatch = min_distance[i - 1][j - 1] + 1
            
            if t[i - 1] == s[j - 1]:
                min_distance[i][j] = min(insertion, deletion, match)
            else:
                min_distance[i][j] = min(insertion, deletion, dismatch)    
    
    return min_distance[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))