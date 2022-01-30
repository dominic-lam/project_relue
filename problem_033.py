from fractions import Fraction

def check_non_trivial(x, y):
    #ab/cd
    lowest_form = Fraction(x,y)
    a = int(str(x)[0])
    b = int(str(x)[1])
    c = int(str(y)[0])
    d = int(str(y)[1])

    if d == 0:
        return False

    if (Fraction(a,d) == lowest_form and b==c) or (Fraction(b,c) == lowest_form and a==d):

        return True

    return False

if __name__ == '__main__':

    fractions = []

    for i in range(11,100):
        for j in range(10,i):
            if check_non_trivial(j, i):
                print(j, i)
                fractions.append(Fraction(j,i))

    product = 1
    for f in fractions:
        product *= f

    print(Fraction(product))
