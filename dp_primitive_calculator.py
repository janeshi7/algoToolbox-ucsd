# Uses python3
import sys

#greedy algo
#def optimal_sequence_greedy(n):
    #sequence = []
    #while n >= 1:
        #sequence.append(n)
        #if n % 3 == 0:
            #n = n // 3
        #elif n % 2 == 0:
            #n = n // 2
        #else:
            #n = n - 1
    #return reversed(sequence)

#dynamic programming
#This function returns a list of tuples (min no. of operation, index of previous element of the optimal sequence
#(also equals to the previous value of optimal sequence))
def optimal_sequence_dp(n,d):
    
    if n == 0:
        #print  ("n < 1")
        return d[0]
    if n == 1:
        #print ("n == 1")
        return d[1]
    for i in range(2, n + 1):
        #print ("i = ", i)
        op_val_p1 = (d[i-1][0] + 1, i - 1)
        op_val = op_val_p1
        #print ("op_val = ", op_val)
        if i % 3 == 0:
            #print ("Yes! dividable by 3")
            op_val_m3 = (d[i // 3][0] + 1, i // 3)
            if op_val_m3[0] < op_val[0]:
                op_val = op_val_m3
            #print ("op_val = ", op_val)
        if i % 2 == 0:
            #print ("Yes! dividable by 2")
            op_val_m2 = (d[i // 2][0] + 1, i // 2)
            if op_val_m2[0] < op_val[0]:
                op_val = op_val_m2
                
            #print ("op_val = ", op_val)

        d[i] = op_val
        #print ("d = ", d)
    
    #print ("d[n] =", d[n])
    return d[n]

#This function returns no. of operations and the optimal sequence
def the_sequence(m):
    #List of tuple initialization
    d = [(0,0)]*(m + 1)
    d[0] = (0, 0)
    d[1] = (0, 1)
    #!!!remember to pass initialization value to function!!!
    a = optimal_sequence_dp(m,d)
    #Create the reversed sequecne is our optimal sequence
    sequence = []
    sequence.append(m)
    i = m
    while i > 1:
        i = d[i][1]
        sequence.append(i) 
    sequence.reverse()
    return d[m][0], sequence

input = sys.stdin.read()
n = int(input)
#The line below is the input line used in jupyter
#n = int(input()) 
op, sequence = the_sequence(n)
print(op)
for x in sequence:
    print(x, end=' ')
