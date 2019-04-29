# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    for i in range(0, len(arr)):
        min_ind = i
        for a in range(i, len(arr)):
            print(arr[a])
            if arr[a] < arr[min_ind]:
                min_ind = a
        temp = arr[i]
        arr[i] = arr[min_ind]
        arr[min_ind] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


selection_sort([4, 2, 6, 1, 7, 9, 8])


"""
[4, 2, 6, 1, 7, 9, 8]
[1, 2, 6, 4, 7, 9, 8]
[1, 2, 6, 4, 7, 9, 8]
"""
