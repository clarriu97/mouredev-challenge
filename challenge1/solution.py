
def sort_string(str):
    return ''.join(sorted(str))


def are_equal(word1: str, word2: str):
    if word1 == word2:
        return True
    return False


def is_anagram(word1: str, word2: str):
    if are_equal(word1, word2):
        return False

    word1 = word1.lower()
    word2 = word2.lower()

    word1 = sort_string(word1)
    word2 = sort_string(word2)

    return are_equal(word1, word2)


t = int(input())

for i in range(0, t):
    word1 = input()
    word2 = input()

    print(is_anagram(word1, word2))
