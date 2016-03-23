def binarySearch(li, v):
    return _binarySearch(li, 0, len(li) - 1, v)

def _binarySearch(li, start, stop, v):
    if start <= stop:
        mid = int((start + stop)/2)
        if li[mid] > v:
            return _binarySearch(li, start, mid - 1, v)
        elif li[mid] < v:
            return _binarySearch(li, mid + 1, stop, v)
        else:
            return mid
    else:
        return -1

def main():
    li = list(range(0,20))
    print(li)
    for v in li:
        print(binarySearch(li, v))

if __name__ == "__main__":
    main()