import random
import array

class KMP():
    def __init__(self, s):
        self._s = s
        self._t = KMP.buildTable(s)

    def __str__(self):
        return self._s

    def buildTable(s):
        t = array.array('l', [0]*len(s))
        t[0] = -1
        t[1] = 0
        p = 2
        c = 0
        while p < len(s):
            if s[p-1] == s[c]:
                t[p] = c + 1
                c = c + 1
                p = p + 1
            elif c > 0:
                c = t[c]
            else:
                t[p] = 0
                p = p + 1
        return t

    def search(self, w):
        m = 0
        i = 0
        while (m + i) < len(self._s):
            if w[i] == self._s[m + i]:
                if i == len(w) - 1:
                    return m
                i = i + 1
            else:
                if self._t[i] > -1:
                    m = m + i - self._t[i]
                    i = self._t[i]
                else:
                    i = 0
                    m = m + 1
        return -1

def main():
    s = "PARTICIPATE IN PARACHUTE"
    kmp = KMP(s)
    
    for i in range(0, len(s)):
        w = s[i:i + random.randint(1,len(s)/2)]
        print("W: {}, P: {}".format(w, kmp.search(w)))

if __name__ == "__main__":
    main()