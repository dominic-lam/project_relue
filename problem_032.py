def get_proper_divisors(n):
    divisors = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

def check_if_pandigital(n):
    divisors = get_proper_divisors(n)

    for d in divisors:
        product = n
        multiplicand = int(n/d)
        multiplier = d
        string = str(n)+str(multiplicand)+str(multiplier)
        list = sorted(string)

        if '0' in list:
            continue

        if not checkIfDuplicates_1(list) and len(list) == 9:
            print(n, multiplicand, multiplier)
            return n

    return 0


if __name__ == '__main__':
    i = 0
    sum = 0
    while i < 10000000:
        #check i
        result = check_if_pandigital(i)
        sum += result
        if result > 0:
            print(sum)
        i+=1

    print(sum)
