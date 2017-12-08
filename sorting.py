#  File: sorting.py
#  Description: Program runs a benchmark test of various sorting algorithms. Output is the result of the test cases
#  Student's Name: Brian Tsai
#  Student's UT EID: byt76
#  Course Name: CS 313E
#  Unique Number: 51465
#
#  Date Created: 11/25/17
#  Date Last Modified: 11/25/17

import random
import time
import sys
sys.setrecursionlimit(10000)

# Bubble sort function
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

# Insertion sort function
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

# Merge sort function
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

# Quick sort function
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


# Return a randomized array of numbers of specified length
def randomize(size):
    list = [number for number in range(size)]
    random.shuffle(list)
    return list

# Return a sorted array of numbers of specified length
def sorted(size):
    list = [number for number in range(size)]
    return list

# Return a reversed array of numbers of specified length
def reverse(size):
    list = [number for number in range(size - 1, -1, -1)]
    return list

# Return a sorted array with 10% of the numbers swapped
def almostSorted(size):
    list = [number for number in range(size)]
    pairs = int(size * 0.1)
    randomIndices = random.sample(range(size), 2 * pairs)
    for times in range(0, len(randomIndices), 2):
        list[randomIndices[times]], list[randomIndices[times + 1]] = list[randomIndices[times + 1]], list[randomIndices[times]]
    return list


sort = {"bubbleSort" : bubbleSort, "insertionSort" : insertionSort, "mergeSort" : mergeSort, "quickSort" : quickSort}
input = {"Random" : randomize, "Sorted" : sorted, "Reverse" : reverse, "Almost sorted" : almostSorted}
sizes = [10, 100, 1000]
def main():

    # Iterate over each type of array
    for inputType in input:
        print("Input type = ", inputType)
        print("                     avg time   avg time   avg time")
        print("   Sort function      (n=10)     (n=100)   (n=1000)")
        print("------------------------------------------------------")

        # Iterate over each sort type
        for sortType in sort:
            print('{:>16}'.format(sortType), end = "     ")

            # Iterate over each size
            for size in sizes:
                average = 0

                # Iterate each size five times and take the average time
                for iteration in range(5):
                    list = input[inputType](size)
                    startTime = time.time()
                    sort[sortType](list)
                    endTime = time.time()
                    elapsedTime = endTime - startTime
                    average += elapsedTime

                # Take the average of all the runs for each sort
                average /= 5
                print('{:.6f}'.format(average), end = "   ")
            print()
        print("\n")
main()