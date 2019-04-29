# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    for i in range(0, len(arr)):
        min_ind = i
        for a in range(i, len(arr)):
            if arr[a] < arr[min_ind]:
                min_ind = a
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(0, len(arr)):
        for a in range(0, len(arr)-1):
            if arr[a] > arr[a+1]:
                arr[a], arr[a+1] = arr[a+1], arr[a]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
