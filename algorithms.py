from visuals import draw_bars
from shared import *


def insertion_sort():
    for i in range(1, len(data)):
        cur = data[i]
        j = i - 1
        while j >= 0 and data[j] > cur:
            data[j + 1] = data[j]
            data[j] = cur
            color_array = ['#00BCF4'] * len(data)
            color_array[j], color_array[j + 1] = '#00BE23', '#00BE23'
            draw_bars(data, color_array)
            time.sleep(speed_scale.get())
            j -= 1
        data[j + 1] = cur
        draw_bars(data, ['#00BE23'] * len(data))
    draw_bars(data, ['#00BE23'] * len(data))
    messagebox.showinfo("Done", "Insertion Sort Completed!")

def selection_sort():
    for i in range(len(data) - 1):
        minIndex = i
        for j in range(i + 1, len(data)):
            # color_array = ['#00BCF4'] * len(data)
            # color_array[minIndex] = '#00BE23'
            # color_array[j] = '#00BE23'
            # draw_bars(data, color_array)
            # time.sleep(speed_scale.get())
            if data[minIndex] > data[j]:
                minIndex = j
        data[i], data[minIndex] = data[minIndex], data[i]
        draw_bars(data, ['#00BCF4'] * len(data))
    draw_bars(data, ['#00BE23'] * len(data))
    messagebox.showinfo("Done", "Selection Sort Completed!")

def bubble_sort():
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            color_array = ['#00BCF4'] * len(data)
            color_array[j] = 'light blue'
            color_array[j + 1] = 'light blue'
            draw_bars(data, color_array)
            time.sleep(speed_scale.get())
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
        draw_bars(data, ['#00BCF4'] * len(data))
    draw_bars(data, ['#00BE23'] * len(data))
    messagebox.showinfo("Done", "Bubble Sort Completed!")


def merge(arr, start, mid, end):
    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]
    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        # Highlight the compared elements
        color_array = ['#00BCF4'] * len(arr)
        # get positions in the original array
        left_idx = start + i
        right_idx = mid + 1 + j
        color_array[left_idx] = '#00BE23'
        color_array[right_idx] = '#00BE23'
        draw_bars(arr, color_array)
        time.sleep(speed_scale.get())

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        color_array = ['#00BCF4'] * len(arr)
        color_array[k] = '#00BE23'  # Highlight the recently moved element
        draw_bars(arr, color_array)
        time.sleep(speed_scale.get())
        k += 1

    while i < len(left):
        arr[k] = left[i]
        color_array = ['#00BCF4'] * len(arr)
        color_array[k] = '#00BE23'
        draw_bars(arr, color_array)
        time.sleep(speed_scale.get())
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        color_array = ['#00BCF4'] * len(arr)
        color_array[k] = '#00BE23'
        draw_bars(arr, color_array)
        time.sleep(speed_scale.get())
        j += 1
        k += 1

def helper_merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        color_array = ['#00BCF4'] * len(arr)
        for i in range(start, end + 1):
            color_array[i] = '#FF6347'
        draw_bars(arr, color_array)
        time.sleep(speed_scale.get())

        helper_merge_sort(arr, start, mid)
        helper_merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)

def merge_sort():
    helper_merge_sort(data, 0, len(data) - 1)
    draw_bars(data, ['#00BE23'] * len(data))
    messagebox.showinfo("Done", "Merge Sort Completed!")