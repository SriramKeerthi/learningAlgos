import random

class FenwickTree():
    def __init__(self, size):
        self._tree = [0 for i in range(0, size)]

    def __str__(self):
        return str(self._tree)

    def sum(self, i):
        sumT = 0
        while i > 0:
            sumT = sumT + self._tree[i - 1]
            i = i - (i & -i)
        return sumT

    def add(self, i, k):
        while i <= len(self._tree):
            self._tree[i - 1] = self._tree[i - 1] + k
            i = i + (i & -i)

def main():
    i = 10
    t = FenwickTree(i)
    for j in range(0, i):
        t.add(j + 1, j + 1)

    print("Tree: {}".format(t))

    for j in range(0, i):
        print("Sum of {} to {}: {}".format(0, j, t.sum(j + 1)))

if __name__ == "__main__":
    main()
