import time, utilities, os

def contain_the_same_digits(nums):
    sorted_s = sorted(str(nums[0]))
    for i in range(1, len(nums)):
        if sorted(str(nums[i])) != sorted_s:
            return False
    return True

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    print(contain_the_same_digits([125874, 251748]))

    for i in range(100000,166666 + 1):
        if not utilities.checkIfDuplicates_1(str(i)):
            ls = []
            for j in range(1,7):
                ls.append(i*j)
            if contain_the_same_digits(ls):
                print(ls)

    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
