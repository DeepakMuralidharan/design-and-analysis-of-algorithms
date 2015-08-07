import time 
start_time = time.time()
inversions = 0
def merge_and_count_split_inv(array, middle, left, right):
    inv = 0
    i = left 
    j = middle + 1
    
    d_array = []
    
    
    while ((i <= middle) and (j <= right)):
        if array[i] < array[j] :
            d_array.append(array[i])
    
            i += 1
        else:
            d_array.append(array[j])
            
            j += 1
            inv += middle - i + 1
            
    
    while (i <= middle):
        d_array.append(array[i])
        i += 1
       
    while (j <= right):
        d_array.append(array[j])
        j += 1
    
    for i in range(0,len(d_array)):
        array[i+left] = d_array[i]
        
    
   
    return inv

def sort_and_count (array, left, right):
  
    middle = (left + right)/2 
    #print middle
    
    if (left == right):
        return 0

    if (left < right):
        
        x = sort_and_count(array, left, middle)
        y = sort_and_count(array, middle + 1, right)
        z = merge_and_count_split_inv(array, middle, left, right)
        
        
    return x + y +z 
        
def mergesort():
    with open('IntegerArray.txt') as f:
        number = []
        for line in f:
            number.append(int(line))
    
    print sort_and_count(number,0,len(number)-1)
    
mergesort()
print time.time() - start_time