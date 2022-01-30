import math

#Todo generate sum of 5th power of a number's digit
def sum_of_5th_power_of_digit(n):
    temp = str(n)
    sum = 0
    digits = []
    for digit in temp:
        result = math.pow((int(digit)),5)
        sum += result
        digits.append(result)
    return sum, digits

if __name__ == '__main__':
    #Todo find the numbers and calculate the sum
    i = 2
    big_limit = math.pow(10,6) #note that 9^5 = 59048, thus the upper bound of those numbers should be about 450k something
    results = []
    while i < big_limit:
        sum, digits = sum_of_5th_power_of_digit(i)
        if sum == i:
            print(i, digits)
            results.append(i)
        i += 1

    sum = 0
    for result in results:
        sum += result
    print(sum)