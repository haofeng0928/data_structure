# 不满足两两比较相邻记录，非标准冒泡排序
def bubble_sort1(a):
    lens = len(a)
    for i in range(lens-1):
        for j in range(i+1, lens):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a


# 标准冒泡排序
def bubble_sort2(a):
    lens = len(a)
    for i in range(lens):
        for j in range(lens-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a


# 冒泡排序优化，增加flag
def bubble_sort(a):
    lens = len(a)
    flag = 1
    for i in range(lens):
        if flag:
            flag = 0
            for j in range(lens-1, i, -1):
                if a[j-1] > a[j]:
                    a[j-1], a[j] = a[j], a[j-1]
                    flag = 1
    return a


def select_sort(a):
    lens = len(a)
    for i in range(lens-1):
        min_index = i
        for j in range(i+1, lens):
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a


def insert_sort(a):
    lens = len(a)
    for i in range(1, lens):
        if a[i] < a[i-1]:
            tem = a[i]
            index = i
            for j in range(i-1, -1, -1):
                if tem < a[j]:
                    a[j+1] = a[j]
                    index = j
            a[index] = tem
    return a


# increment = 1时，即为插入排序
def shell_sort(a):
    increment = len(a)
    while increment > 1:
        increment = increment // 3 + 1
        for i in range(increment, len(a)):
            if a[i] < a[i-increment]:
                tem = a[i]  # 待插入元素
                index = i
                for j in range(i-increment, -1, -increment):
                    if tem < a[j]:
                        a[j+increment] = a[j]
                        index = j
                a[index] = tem
    return a


def shell_sort2(a):
    gap = len(a)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(a)):
            index = i
            while index >= gap and a[index] < a[index-gap]:  # 直接交换位置
                a[index], a[index-gap] = a[index-gap], a[index]
                index -= gap
    return a


def heap_sort(a):
    lens = len(a)
    for i in range(lens//2-1, -1, -1):
        _heap_adjust(a, i, lens)
    for i in range(lens-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        _heap_adjust(a, 0, i)
    return a


def _heap_adjust(a, i, lens):
    tem = a[i]
    j = 2 * i + 1
    while j <= lens-1:  # 严格的大顶堆
        if j < lens-1 and a[j] < a[j+1]:
            j += 1
        if tem >= a[j]:
            break
        a[i] = a[j]
        i = j
        j = 2 * j + 1
    a[i] = tem


# 递归
def heap_sort2(a):
    _heap_adjust2(a, len(a))
    return a


def _heap_adjust2(a, lens):
    if lens <= 1:
        return
    index = lens // 2 - 1
    for i in range(index, -1, -1):
        j = 2 * i + 1
        if j < lens - 1 and a[j] < a[j + 1]:
            j += 1
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
    a[0], a[lens - 1] = a[lens - 1], a[0]
    _heap_adjust2(a, lens - 1)  # 一次排序得到的并不是一个严格的大顶堆


# 递归
def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return _merge(left, right)  # 子序列长度为1时，执行_merge函数，并返回上层递归


def _merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:] + right[j:]
    return result


# 非递归
def merge_sort2(a):
    lens = len(a)
    step = 1
    while step < lens:
        low = 0
        while low < lens:
            mid = low + step
            high = min(low + 2 * step, lens)
            if mid < high:
                _merge2(a, low, mid, high)
            low += 2 * step
        step *= 2
    return a


def _merge2(a, low, mid, high):
    left = a[low: mid]
    right = a[mid: high]
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:] + right[j:]
    a[low: high] = result


def quick_sort(a):
    _qsort(a, 0, len(a)-1)
    return a


def _qsort(a, low, high):
    # 优化小数组时的排序方案
    # min_len = 7
    # if (high-low) > min_len:
    #     pass
    # else:
    #     insert_sort(a)
    if low < high:
        index = _partition(a, low, high)
        _qsort(a, low, index-1)
        _qsort(a, index+1, high)


# 优化递归操作，尾递归
# def _qsort(a, low, high):
#     while low < high:
#         index = _partition(a, low, high)
#         _qsort(a, low, index-1)
#         low = index + 1


def _partition(a, low, high):
    # 优化选取枢轴，三数取中
    # mid = (low + high) // 2
    # if a[low] > a[high]:
    #     a[low], a[high] = a[high], a[low]
    # if a[mid] > a[high]:
    #     a[mid], a[high] = a[high], a[mid]
    # if a[mid] < a[low]:
    #     a[mid], a[low] = a[low], a[mid]
    tem = a[low]
    while low < high:
        while low < high and a[high] >= tem:
            high -= 1
        a[low] = a[high]
        while low < high and a[low] <= tem:
            low += 1
        a[high] = a[low]
    a[low] = tem
    return low


def quick_sort2(a):
    _qsort2(a, 0, len(a)-1)
    return a


def _qsort2(a, start, end):
    if start >= end:
        return
    tem = a[start]
    left = start
    right = end
    while left < right:
        while left < right and a[right] >= tem:
            right -= 1
        a[left] = a[right]
        while left < right and a[left] <= tem:
            left += 1
        a[right] = a[left]
    a[left] = tem
    _qsort2(a, start, left - 1)
    _qsort2(a, left + 1, end)


print('bubble_sort1 = ', bubble_sort1([5, 1, 9, 3, 7, 4, 8, 6, 2]))
print('bubble_sort2 = ', bubble_sort2([5, 1, 9, 3, 7, 4, 8, 6, 2]))
print('bubble_sort  = ', bubble_sort([5, 1, 9, 3, 7, 4, 8, 6, 2]))
print('select_sort  = ', select_sort([5, 1, 9, 3, 7, 4, 8, 6, 2]))
print('insert_sort  = ', insert_sort([5, 1, 9, 3, 7, 4, 8, 6, 2]))
print('shell_sort   = ', shell_sort([5, 1, 9, 3, 7, 4, 8, 6, 2]))
print('shell_sort2  = ', shell_sort2([5, 1, 9, 3, 7, 4, 8, 6, 2]))
print('heap_sort    = ', heap_sort([5, 1, 9, 3, 7, 4, 8, 6, 2]))
print('heap_sort2   = ', heap_sort2([5, 1, 9, 3, 7, 4, 8, 6, 2]))
print('merge_sort   = ', merge_sort([5, 1, 9, 3, 7, 4, 8, 6, 2]))
print('merge_sort2  = ', merge_sort2([5, 1, 9, 3, 7, 4, 8, 6, 2]))
print('quick_sort   = ', quick_sort([5, 1, 9, 3, 7, 4, 8, 6, 2]))
print('quick_sort2  = ', quick_sort2([5, 1, 9, 3, 7, 4, 8, 6, 2]))

