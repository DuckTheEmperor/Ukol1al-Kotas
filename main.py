import random
import bubble_sort
array = [4, 87, 31, 70, 96, 11, 2, 42, 63, 28]

def bubble_sort():
    n=len(array)
    for i in range(n-1):
        for j in range (0, n-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1]=array[j+1], array[j]
    return array

print(bubble_sort())

arrayb = [88, 76, 3, 90, 21, 10, 1, 65, 43, 28]
def is_sorted(arrayb):
    for i in range(1, len(arrayb)):
        if arrayb[i] < arrayb[i-1]:
            return False
    return True

def bogosort(arrayb):
    count = 0
    while not is_sorted(arrayb):
        random.shuffle(arrayb)
        count += 1
        print(f"Pokus {count}: {arrayb}")
    print(f"seznam serazen po {count} pokusech")

bogosort(arrayb)

print("Bogo", arrayb)

array = [45, 56, 47, 64, 8, 68, 75, 24, 2, 68]

def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
         
            if array[j] < array[min_index]:
                min_index = j
        
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
