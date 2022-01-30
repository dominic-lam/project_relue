import math

def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

def check_if_1_to_9_pandigital(string):
    list = sorted(string)

    if '0' in list:
        return False

    if not checkIfDuplicates_1(list) and len(list) == 9:
        return True

def check_if_1_to_7_pandigital(string):
    list = sorted(string)

    if '0' in list or '8' in list or '9' in list:
        return False

    if not checkIfDuplicates_1(list) and len(list) == 7:
        return True


def is_prime(n):
    if n <= 1:
        return False

    if n%2 == 0:
        return False

    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    if sum%3 == 0:
        return False

    for i in range(5, math.sqrt(n).__int__() + 1):
        if n%i == 0:
            return False

    return True

if __name__ == '__main__':
    #Note that sum from 1 to 9 = 45 which is divisible by 3, there is no number 9 digit pandigital and prime simutaneously
    #Similarly, not prime is 8 digit pandigital
    #Street smart, we start from 7 digits number work backward to find the largest prime
    big_n = int(math.pow(10,7))
    for i in range(big_n - int(big_n/100),1,-1):
        if check_if_1_to_7_pandigital(str(i)):
            print(i, 'is 1 to 7 pandigital')
            if is_prime(i):
                print(i, 'is also a prime')
                break
