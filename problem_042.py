import utilities

def setup_word_list():
    f = open('problem_042_words.txt', 'r')
    temp_words = f.read()
    temp_words = temp_words.replace('"', '')
    word_list = temp_words.split(',')
    return word_list

if __name__ == '__main__':
    word_list = setup_word_list()
    triangle_word_list = []
    for word in word_list:
        word_value = 0
        for alphabet in word:
            word_value += utilities.get_alphabet_value(alphabet)
        if utilities.is_triangle_number(word_value):
            triangle_word_list.append((word,word_value))

    for triangle_word in triangle_word_list:
        print(triangle_word)

    print(len(triangle_word_list))
