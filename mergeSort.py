import random

def _mergeSort(li):
    if len(li) <= 1:
        return li
    else:
        partition = int(len(li)/2)
        return _merge(_mergeSort(li[0:partition]), _mergeSort(li[partition:]))

def _merge(li1, li2):
    li = []
    i = 0
    j = 0
    while i < len(li1) and j < len(li2):
        if li1[i] < li2[j]:
            li.append(li1[i])
            i = i + 1
        else:
            li.append(li2[j])
            j = j + 1
    if i == len(li1):
        li.extend(li2[j:])
    else:
        li.extend(li1[i:])
    return li

def mergeSort(li):
    newList = list(li)
    return _mergeSort(newList)

def main():
    li = list(range(0,30))
    random.shuffle(li)
    print(li)
    print(mergeSort(li))

if __name__ == "__main__":
    main()