def setup_name_list():
    f = open('problem_022_names.txt', 'r')
    temp_names = f.read()
    temp_names = temp_names.replace('"', '')
    name_list = temp_names.split(',')
    name_list = sorted(name_list)
    return name_list

def get_name_value(name:str):
    numbers = []
    sum = 0
    for letter in name:
        number = ord(letter) - 64
        numbers.append(number)
        sum += number
    return numbers, sum

if __name__ == '__main__':
    name_list = setup_name_list()
    print(name_list)
    total_name_scores = 0
    for i in range(0, len(name_list)):
        position = i+1
        name = name_list[i]
        (numbers, sum) = get_name_value(name)
        name_scores = position*sum
        print(position, name, numbers, sum, name_scores)

        total_name_scores += name_scores

    print(total_name_scores)