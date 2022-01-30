import math

if __name__ == '__main__':
    k = math.pow(2,1000).__int__()
    ls = str(k)
    sum = 0
    for i in ls:
        sum += int(i)
    print(sum)