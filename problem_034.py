import math
def is_curious(n:int):
    s = str(n)
    sum = 0
    for i in s:
        sum += math.factorial(int(i))
    if sum == n:
        return True
    return False

if __name__ == '__main__':
    sum = 0
    for i in range(3,5000000):
        if is_curious(i):
            print(i)
            sum += i
    print(sum)
