import random

class RabinKarp:
    def _hash(s):
        return RabinKarp._roll(s, 0, 0, len(s) - 1)

    def _roll(s, oldHash, start, stop):
        hashVal = 0
        if start == 0:
            for i in range(start, stop + 1):
                hashVal = hashVal * 101 + ord(s[i])
        else:
            width = stop - start
            hashVal = (oldHash - (ord(s[start-1]) * pow(101, width))) * 101 + ord(s[stop])
        return hashVal

    def search(s, p):
        pHash = RabinKarp._hash(p)
        sHash = 0
        for i in range(0, len(s) - len(p) + 1):
            sHash = RabinKarp._roll(s, sHash, i, i + len(p) - 1)
            if sHash == pHash and s[i:i+len(p)] == p:
                return i
        return -1

def main():
    s = "PARTICIPATE IN PARACHUTE"
    for i in range(0, len(s)):
        p = s[i:i + random.randint(1,len(s)/2)]
        print("W: {}, P: {}".format(p, RabinKarp.search(s, p)))

if __name__ == "__main__":
    main()
