import time, utilities, os
import math
def sum_of_digits_factorial(n):
    sum = 0
    for s in str(n):
        sum += math.factorial(int(s))
    return sum
if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    chain_list = []
    for i in range(0,1000000):
        chain = [i]
        counter = 0
        j = 1
        sum = i
        while True:
            sum = sum_of_digits_factorial(sum)
            if not sum in chain:
                chain.append(sum)
            else:
                break
            j+=1
        if len(chain) == 60:
            chain_list.append(chain)

    for list in chain_list:
        print(list)

    print(len(chain_list))

    #idea, create another list to store the "recurring" number,
    # record the chain before meeting the same number again


    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
