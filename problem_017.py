from num2words import num2words

if __name__ == '__main__':
    sum = 0
    for i in range(1,1000+1):
        word = num2words(i)
        print(word)
        word = word.replace(' ', '')
        word = word.replace('-', '')
        sum += len(word)

    print(sum)