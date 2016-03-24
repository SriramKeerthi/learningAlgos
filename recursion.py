def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    for i in range(1,10):
        print(factorial(i))

if __name__ == "__main__":
    main()