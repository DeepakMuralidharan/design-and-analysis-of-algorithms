#import time 
#start_time = time.time()
comparisons = 0

def partition_around_pivot(array,left,right):
    global comparisons
    comparisons = comparisons + right - left 
    pivot = array[left]
    i = left + 1
    for j in range(left+1,right+1):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp 
            i = i + 1
    
    temp = array[left]
    array[left] = array[i-1]
    array[i-1] = temp 
    pos = i-1
    return pos 
    
    
def quick_sort(array, left, right):
      
    if (left == right):
        return 0

    if (left < right):
        pos = partition_around_pivot(array, left, right)
        quick_sort(array, left, pos-1)
        quick_sort(array, pos + 1, right)
        
        
        
        
    return array
        
def quicksort():
    with open('QuickSort.txt') as f:
        number = []
        for line in f:
            number.append(int(line))
    #number = [3,8,2,5,1,4,7,6]
    print quick_sort(number,0,len(number)-1)
 
    
quicksort()
print comparisons#print time.time() - start_time