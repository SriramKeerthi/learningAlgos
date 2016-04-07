import random

def toBin(i):
    s = ""
    while i > 0:
        s = str(i % 2) + s
        i = int(i / 2)
    return ("0" * (16 - len(s))) + s

def main():
    i = 10
    print(toBin(i))
    
if __name__ == "__main__":
    main()