import random

def quickSort(li):
    newList = list(li)
    _quickSort(newList, 0, len(li) - 1)
    return newList

def _getPivot(li, startIndex, stopIndex):
    return li[int((startIndex + stopIndex)/2)]

def _partition(li, startIndex, stopIndex):
    pivot = _getPivot(li, startIndex, stopIndex)
    while True:
        while li[startIndex] < pivot:
            startIndex = startIndex + 1
        while li[stopIndex] > pivot:
            stopIndex = stopIndex - 1
        if startIndex >= stopIndex:
            return stopIndex
        _swap(li, startIndex, stopIndex)
        startIndex = startIndex + 1
        stopIndex = stopIndex - 1

def _swap(li, i, j):
    temp = li[i]
    li[i] = li[j]
    li[j] = temp

def _quickSort(li, startIndex, stopIndex):
    if startIndex < stopIndex:
        partition = _partition(li, startIndex, stopIndex)
        _quickSort(li, startIndex, partition)
        _quickSort(li, partition + 1, stopIndex)

def main():
    li = list(range(0,20))
    random.shuffle(li)
    print(li)
    print(quickSort(li))

if __name__ == "__main__":
    main()