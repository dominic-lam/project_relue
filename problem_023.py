def get_proper_divisors(n):
    divisors = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def sum_of_list(list:[int]):
    sum = 0
    for i in list:
        sum += i
    return sum

def get_abundant_numbers():
    abundant_numbers = []
    for i in range(1, 28123 + 1):
        divisors = get_proper_divisors(i)
        sum_of_divisors = sum_of_list(divisors)
        if sum_of_divisors > i:
            abundant_numbers.append(i)
    return abundant_numbers

if __name__ == '__main__':
    abundant_numbers = get_abundant_numbers()
    target_numbers_sum = 0

    for i in range(1, 28123+1):
        is_sum_of_two_abandant_number = False

        for j in abundant_numbers:
            if j > i:
                break

            if i > j and ((i-j) in abundant_numbers):
                print(i, j, i-j)
                is_sum_of_two_abandant_number = True
                break

        if not is_sum_of_two_abandant_number:
            target_numbers_sum += i


    print(target_numbers_sum)
