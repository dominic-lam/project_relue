import math

if __name__ == '__main__':
    k = math.factorial(100)
    str = k.__str__()
    sum = 0
    for digit in str:
        sum += int(digit)
    print(sum)
