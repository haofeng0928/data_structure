# 顺序表查找
def SequentialSearch(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i


alist = [1, 3, 5, 7, 9, 8, 6, 4, 2]
result = SequentialSearch(alist, 9)
print(result)


# 二分查找 & 插值查找
def BinarySearch(alist, key):
    # 定义左右下标
    left = 0
    right = len(alist) - 1

    count = 0

    while left <= right:

        #         # 二分查找
        #         mid = (left+right) // 2

        # 插值查找
        mid = left + (right - left) * (key - alist[left]) // (alist[right] - alist[left])

        count += 1

        # 与key比较大小，滑动游标
        if alist[mid] > key:
            right = mid - 1
        elif alist[mid] < key:
            left = mid + 1
        else:
            print('count: ', count)
            return mid

    return False


alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = BinarySearch(alist, 5)
print(result)


# 斐波那契查找
# 时间复杂度O(logn)
def FibonacciSearch(alist, key):
    # 给出一段斐波那契数列，元素个数要大于alist中元素的个数
    F = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
         46368]

    left = 0
    right = len(alist) - 1

    # location为right在斐波那契数列的位置
    location = 0
    while right > F[location] - 1:
        location += 1
    print('location:', location)

    # 为了使alist满足斐波那契特性
    # 在alist的末尾添加F[location]-1-right个alist[right]
    tem = right
    while F[location] - 1 > tem:
        alist.append(alist[right])
        tem += 1
    print('new alist:', alist)

    count = 0

    while left <= right:

        count += 1

        # 防止F下标溢出
        if location < 2:
            mid = left
        else:
            mid = left + F[location - 1] - 1
        print("left=%s, mid=%s, right=%s" % (left, mid, right))

        # 主程序
        # key较小时right左移
        if key < alist[mid]:
            right = mid - 1
            location -= 1

        # key较大时left右移
        elif key > alist[mid]:
            left = mid + 1
            location -= 2

        # key相等时
        else:
            if mid <= right:
                print("count:", count)
                return mid
            else:
                print("count:", count)
                return right

    print("count:", count)
    return False


if __name__ == '__main__':
    alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = FibonacciSearch(alist, 9)
    print(result)

