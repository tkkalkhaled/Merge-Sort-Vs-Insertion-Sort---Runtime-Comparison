# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 13:03:39 2025

@author: Talal
"""

import timeit, random
import matplotlib.pyplot as plt # https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html

## INSERTION SORT VIA https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm/
# Function to sort array using insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
        
## MERGE SORT VIA https://www.geeksforgeeks.org/dsa/merge-sort/
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        
    i = 0  
    j = 0  
    k = left  

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)
        
Size_of_N = [10,50,100,200,500,1000,2000,5000,10000] # Random Sizes 

print("N            Insertion Sort            Merge Sort")

s = list()
ins_time = list()
m_time = list()

for x in Size_of_N:
    ## Now we need to make a random list of N numbers
    
    lst = list()
    for y in range(x):
        lst.append(random.randint(0, 50000)) # generate and append random numnber between 0 and 50k
    
    
    ## NOW TO TEST INSERTION SORT TIMING
    # Source for examples of using timeit https://www.geeksforgeeks.org/python/timeit-python-examples/
    
    starting = timeit.default_timer() # start timer
    insertionSort(lst[:]) ## Call insertion sort on a copy (to keep original list)
    ending = timeit.default_timer() # end timer
    
    insert_time = ending - starting # find diff and thats our time
    
    ## NOW TO TEST MERGE SORT TIMING
    # Source for examples of using timeit https://www.geeksforgeeks.org/python/timeit-python-examples/
    
    starting = timeit.default_timer() # start timer
    mergeSort(lst[:], 0, len(lst) - 1) ## Call merge sort on a copy and make starting index at 0 till length of the list - 1
    ending = timeit.default_timer() # end timer
    
    merge_time = ending - starting # find diff and thats our time
    
    ## Update values of list to plot table
    s.append(x)
    ins_time.append(insert_time)
    m_time.append(merge_time)
    
    ## Print table
    print(x,"            ",round(insert_time, 7), "            ", round(merge_time,7)) ## I rounded to make it readible
    

## Plotting Merge Sort Vs Insetion Sort https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html
plt.plot(Size_of_N, ins_time, label="Insertion Sort")
plt.plot(Size_of_N, m_time, label="Merge Sort")

plt.xlabel("Array size (n)")
plt.ylabel("Time (seconds)")
plt.title("Merge Sort vs Insertion Sort")
plt.legend()
plt.show()
        
## Hybrid Sorting -- If n > 100 , then we use merge sort
## Tim sort

print("N            Hybrid Sort")

sizes_ins = list()
times_ins = list()

sizes_mer = list()
times_mer = list()

for x in Size_of_N:
    ## Now we need to make a random list of N numbers
    
    lst = list()
    for y in range(x):
        lst.append(random.randint(0, 50000)) # generate and append random numnber between 0 and 50k
    
    
    if x < 100: # here we use insertion sort
        # Source for examples of using timeit https://www.geeksforgeeks.org/python/timeit-python-examples/
        
        starting = timeit.default_timer() # start timer
        insertionSort(lst[:]) ## Call insertion sort on a copy (to keep original list)
        ending = timeit.default_timer() # end timer
        
        hybrid_time = ending - starting # find diff and thats our time
        
        sizes_ins.append(x)
        times_ins.append(hybrid_time)
        print(x, "     ", round(hybrid_time, 7), "   (Insertion)")
    
    ## NOW TO TEST MERGE SORT TIMING
    # Source for examples of using timeit https://www.geeksforgeeks.org/python/timeit-python-examples/
    else:
        # if n > 100 then we use merge sort
        starting = timeit.default_timer() # start timer
        mergeSort(lst[:], 0, len(lst) - 1) ## Call merge sort on a copy and make starting index at 0 till length of the list - 1
        ending = timeit.default_timer() # end timer
        
        merge_time = ending - starting # find diff and thats our time
        
        sizes_mer.append(x)
        times_mer.append(merge_time)
        print(x, "     ", round(hybrid_time, 7), "   (Merge)")
    
    
    
    

## Plotting Merge Sort Vs Insetion Sort https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html
plt.plot(sizes_ins, times_ins, label="Insertion Sort")
plt.plot(sizes_mer, times_mer, label="Merge Sort")

plt.xlabel("Array size (n)")
plt.ylabel("Time (seconds)")
plt.title("Hybrid decision: use Merge when n > 100")
plt.legend()
plt.show()
        
        
        
        
        
