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

if __name__ == '__main__':
    numbers = []
    for i in range(1,9999):
        s = ''
        j = 1
        while len(s) < 9:
            s += str(i*j)
            j += 1
        if len(s) == 9 and check_if_1_to_9_pandigital(s):
            numbers.append(int(s))

    numbers = sorted(numbers)
    print(numbers[-1])