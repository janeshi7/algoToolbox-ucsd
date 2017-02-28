# Uses python3
import sys

def merge_and_count_inversions(x, y):
    sorted_array = [] 
    count = 0 
    i, j = 0, 0
    print ("inside merge", x, y)
    while i < len(x) and j < len(y):
        if x[i] > y[j]:
            count += len(x) - i
            sorted_array.append(y[j])
            j += 1
        else:
            sorted_array.append(x[i])
            i += 1
    while i < len(x):
        sorted_array.append(x[i])
        i += 1
    while j < len(y):
        sorted_array.append(y[j])
        j += 1
    print ("overall count = ", count )
    print ("sorted_array", sorted_array)
    return count, sorted_array
            
def get_number_of_inversions(a, b, left, right):
    print ("wow, new round!")
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions, a[left:right]
    ave = (left + right) // 2
    print ("ave = ", ave)
    number_of_inversions_A, a[left:ave] = get_number_of_inversions(a, b, left, ave)
    number_of_inversions += number_of_inversions_A
    print ("left list", a[left : ave])
    print ("number_of_inversions A = ", number_of_inversions )
    number_of_inversions_B, a[ave:right] = get_number_of_inversions(a, b, ave, right)
    number_of_inversions += number_of_inversions_B
    print ("right list", a[ave : right])
    print ("number_of_inversions A+B = ", number_of_inversions )
    number_of_inversions_C, sorted_list = merge_and_count_inversions(a[left:ave],a[ave:right])
    number_of_inversions += number_of_inversions_C
    print ("number_of_inversions A+B+C = ", number_of_inversions )
    return number_of_inversions, sorted_list

input_ = input()
n, *a = list(map(int, input_.split()))
b = n * [0]
get_number_of_inversions(a, b, 0, len(a))
print(get_number_of_inversions(a, b, 0, len(a)))