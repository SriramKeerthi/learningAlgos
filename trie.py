# Word list downloaded from http://wordlist.aspell.net/

import random
import time

class Trie():
    def __init__(self, value=''):
        self._wc = 0
        self._pc = 0
        self._value = value
        self._children = {}

    def __str__(self):
        return "Trie(wordCount={}, prefixCount={}, value={}, children={})".format(self._wc, self._pc, self._value, self._children)

    def __repr__(self):
        return self._value

    def addWord(self, w):
        if len(w) > 0:
            self._pc += 1
            if w[0] not in self._children:
                self._children[w[0]] = Trie(w[0])
            self._children[w[0]].addWord(w[1:])
        else:
            self._wc += 1

    def getWordCount(self, w):
        if len(w) == 0:
            return self._wc
        elif w[0] not in self._children:
            return 0
        else:
            return self._children[w[0]].getWordCount(w[1:])

    def getPrefixCount(self, w):
        if len(w) == 0:
            return self._pc
        elif w[0] not in self._children:
            return 0
        else:
            return self._children[w[0]].getPrefixCount(w[1:])

    def getPrefixWords(self, w):
        if len(w) == 0:
            return subWords()

    def search(self, prefix):
        sx = prefix
        node = self
        while len(sx) > 0:
            if sx[0] in node._children:
                node = node._children[sx[0]]
                sx = sx[1:]
            else:
                return []
        sx = prefix[:-1]
        return [sx + w for w in node._getNodeWords()]

    def _getNodeWords(self):
        words = []
        if self._wc > 0:
            words.append(self._value)
        for child in self._children:
            words.extend([self._value + w for w in self._children[child]._getNodeWords()])
        return words

def main():
    startTime = time.time()
    breakWord = "aspartic"
    print("Loading Trie with dictionary...")
    t = Trie()
    sList = []
    for line in open("english-words.95", "r"):
        w = "".join([c for c in line if ord(c) >= 97 and ord(c) <= 122])
        t.addWord(w)
        if random.randint(0,10000) == 0:
            sList.append(w)
    print("Trie loaded in {}ms".format(int((time.time() - startTime) * 1000)))
    for w in [w[:int(len(w) / 1.5)] for w in sList]:
        wList = t.search(w)
        if len(wList) > 6:
            print("W: {}, WC: {}, PC: {}, WS: {}(...{} more)".format(w, t.getWordCount(w), t.getPrefixCount(w), wList[:5], len(wList) - 5))
        else:
            print("W: {}, WC: {}, PC: {}, WS: {}".format(w, t.getWordCount(w), t.getPrefixCount(w), wList))

if __name__ == "__main__":
    main()
