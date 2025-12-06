def mul_digit(n):
    res = 1
    while n != 0:
        digit = n % 10
        n //= 10
        if digit != 0: 
            res *= digit
    return res

def main ():
    for _ in range(int(input())):
        n = int(input())
        print(mul_digit(n))

if __name__ == "__main__":
    main()