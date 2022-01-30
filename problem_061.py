import time, utilities, os, itertools

def gen_all_numbers():

    numbers_list = []

    for i in range(8, 3-1, -1):
        j = 1
        numbers = []
        while True:
            if utilities.get_n_th_polygonal(j,i) < 1000:
                j += 1
                continue
            if utilities.get_n_th_polygonal(j,i) > 10000:
                break
            numbers.append(utilities.get_n_th_polygonal(j,i))
            j+=1
        numbers_list.append(numbers)

    return numbers_list



def check_numbers_are_cyclic(numbers:list):
    is_cyclic = True
    for i in range(len(numbers)):
        current_index = i
        next_index = i+1
        if i == len(numbers) - 1:
            next_index = 0

        current = numbers[current_index]
        next = numbers[next_index]

        if int(current % 100) != int(next / 100):
            is_cyclic = False
            break

    return is_cyclic

def check_numbers_set_satisfied(numbers):
    if utilities.checkIfDuplicates_1(numbers):
        return False

    perms = utilities.get_permuations_of_list(numbers)
    for p in perms:
        if check_numbers_are_cyclic(p):
            print(p, 'is cyclic')
            return True

    print(numbers, 'Not satisfied')
    return False

def find_solution(start, foo):
    solution = [start]
    for x in range(5):
        numbers_list = foo
        for i in range(len(numbers_list)):

            numbers = numbers_list[i]
            for j in numbers:

                if x == 4:
                    if (int(j%100) == int(start/100)) and (int(solution[x]%100) == int(j/100)):
                        solution.append(j)
                        # print(j, i, len(numbers_list))
                        del numbers_list[i]
                        break
                else:

                    if int(solution[x]%100) == int(j/100):
                        solution.append(j)
                        # print(j, i, len(numbers_list))
                        del numbers_list[i]
                        break

            if len(solution) == x+2:
                break

        if len(solution) != x+2:
            break

    if len(solution) == 6:
        if check_numbers_are_cyclic(solution):
            return solution

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()


    numbers_list = gen_all_numbers()
    for numbers in numbers_list:
        print(len(numbers), numbers)


    for p_8 in numbers_list[5]:
        solution = find_solution(p_8, numbers_list[0:5])
        if solution != None:
            print(sum(solution), solution)
            break






    #Let's try the example case first
    # P_3: 8128, P_5: 2882, P_4: 8281
    #Note, They must be all different

    #1. gen all 4 digits numbers
    #2. pick one to be the first of the set
    #3. check cyclic and pick next

    # for i in numbers_list[0]:
    #     solutions = [i]
    #     for j in range(1,3):
    #         for k in numb

#28684

# numbers_list = gen_all_numbers()
    # for numbers in numbers_list:
    #     print(numbers)
    # solutions = []
    # for i in numbers_list[0]:
    #    for j in numbers_list[1]:
    #        if int(j/100) == int(i%100):
    #            for k in numbers_list[2]:
    #                if int(k/100) == int(j%100) and int(i/100) == int(k%100):
    #                    solutions = [i,j,k]
    #                    print(sum(solutions), solutions)
    #                    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
    #                    exit()
    #                else:
    #                    continue
    #        else:
    #            continue


    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
