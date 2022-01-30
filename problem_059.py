import time, utilities, os
from itertools import permutations

def get_possible_keys():
    chracter_list = [chr(x) for x in range(97, 123)]
    return list(permutations(chracter_list,3))


if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()


    data = utilities.read_data_from_file('problem_059_cipher.txt')
    data = data.split(',')
    data = [int(x) for x in data]
    data = [79,59,12,2,79,35,8,28,20,2,3,68,8,9,68,45,0,12,9,67,68]

    possible_keys = get_possible_keys()

    print(possible_keys[0]*(int(len(data)/3) + 1))
    for possible_key in possible_keys:
        decrypted_msg = ''
        for d,k in zip(data,possible_key*(int(len(data)/3) + 1)):
            decrypted_msg += str(chr(d^ord(k)))

        if 'The' in decrypted_msg:
            print(possible_key, decrypted_msg)


    #(The Gospel of John, chapter 1)


    # print(get_possible_keys_ascii())
    #
    # a = ("John", "Charles", "Mike")
    # b = ("Jenny", "Christy")
    #
    #
    # x = zip(a, b)
    # for (i,j) in x:
    #     print(i,j)

    #
    # print(ord('a'), ord('z')) #so we know
    # print(chr(97), chr(122))
    #
    #
    # chracter_list = [chr(x) for x in range(97, 123)]
    # possible_keys_chr = list(permutations(chracter_list,3))
    # possible_keys_ascii = []
    # for key in possible_keys_chr:
    #     key_in_ascii = ''
    #     for char in key:
    #         key_in_ascii += str(ord(char))
    #     possible_keys_ascii.append(int(key_in_ascii))
    #
    # print(possible_keys_ascii)
    #
    # for key_ascii in possible_keys_ascii:
    #     decrypted_text = ''
    #     for ord_str in data:
    #         k = int(ord_str)
    #         # print(k, type(k))
    #         # print(key_ascii, type(key_ascii))
    #         # print(chr(k^key_ascii))
    #         decrypted_char_ascii = k^key_ascii
    #
    #         if decrypted_char_ascii not in range(0x110000):
    #             break
    #
    #         decrypted_char = chr(decrypted_char_ascii)
    #         decrypted_text += decrypted_char
    #
    #     if 'is' in decrypted_text:
    #         print(decrypted_text, key_ascii)
    #         print('hi')
    #
    #
    # # text = ''
    # # a = chr(36^979899)
    # # print(a)
    # # text += a


    # ls = [1,2,3]
    # print(sum(ls))



    print("---Time spent:  %s seconds ---" % (time.time() - start_time))