import itertools

def get_lexicographic_permutations():
    elemnts = list(range(0,10))
    permutations = list(itertools.permutations(elemnts))
    return permutations

if __name__ == "__main__":
    permutations = get_lexicographic_permutations()
    target_row = permutations[999999]
    ans = ''
    for i in target_row:
        ans += str(i)
    print(ans) #2783915460