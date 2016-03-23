import random

def compare(s, t):
    n = min(len(s), len(t))
    for i in range(0,n):
        if s[i] < t[i]:
            return -1
        if s[i] > t[i]:
            return 1
    return len(s) - len(t)

class Suffix():
    def __init__(self, s, i):
        self._s = s
        self.i = i

    def __len__(self):
        return len(self._s) - self.i

    def __getitem__(self, ix):
        return self._s[ix + self.i]

    def __lt__(self, other):
        if self == other:
            return False
        n = min(len(self), len(other))
        for i in range(0,n):
            if self[i] < other[i]:
                return True
            if self[i] > other[i]:
                return False
        return len(self) - len(other) < 0

    def __str__(self):
        return self._s[self.i:]

    def __repr__(self):
        return self.__str__()

class SuffixArray():
    def __init__(self, s):
        self.suffixes = sorted([Suffix(s,i) for i in range(0, len(s))])

    def __len__(self):
        return len(self.suffixes)

    def __getitem__(self, i):
        return str(self.suffixes[i])

    def index(self, i):
        return self.suffixes[i].i

    def lcp(self, i):
        return SuffixArray._lcp(self.suffixes[i], self.suffixes[i-1])

    def _lcp(s, t):
        n = min(len(s), len(t))
        for i in range(0, n):
            if s[i] != t[i]:
                return i
        return n

    def rank(self, q):
        lo = 0
        hi = len(self) - 1
        while lo <= hi:
            mid = lo + int((hi - lo) / 2)
            cmp = compare(q, self.suffixes[mid])
            if cmp < 0:
                hi = mid - 1
            elif cmp > 0:
                lo = mid + 1
            else:
                return mid
        return lo

    def search(self, q):
        return self.suffixes[self.rank(q)]

def main():
    s = "APPLY YOURSELF! NO APPLES WITHOUT APPLICATION!"
    print("STR: " + s)
    suffix = SuffixArray(s)
    for i in range(0, 10):
        idx = random.randint(0,len(s))
        q = s[idx:idx + random.randint(1,10)]
        suf = suffix.search(q)
        print("Q: {}, Index: {}, Sub: {}".format(q, suf.i, suf))

if __name__ == "__main__":
    main()