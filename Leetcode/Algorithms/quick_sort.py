def qs(arr, low, high):
    if low < high:
        pt_index = pt(arr, low, high)

        qs(arr, low, pt_index - 1)
        qs(arr, pt_index + 1, high)


def pt(arr, low, high):
    # seperating the smaller and greater values respective to the pivot
    pivot = arr[low]
    i, j = low, high

    while i < j:
        while i <= high and arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    arr[low], arr[j] = arr[j], arr[low]
    return j


arr_t = [4, 1, 3, 9, 7]
qs(arr_t, 0, len(arr_t) - 1)
print(arr_t)
