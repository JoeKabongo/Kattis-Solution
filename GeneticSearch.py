# problem description: https://open.kattis.com/problems/geneticsearch
def count_substring(string1, string2):
    """
    count how many substring of string2 equals string1
    :param string1:
    :param string2:
    :return:
    """
    l = len(string2)
    s = len(string1)
    result = 0
    for i in range(l):
        if i + s > l:
            break
        if string1 == string2[i:i+s]:
             result += 1
    return result

while True:

    #grabbing the input
    strings = input().split()
    S = strings[0]
    if S == '0':
        break
    L = strings[1]

    l_length = len(L)
    s_length = len(S)

    #same string, type1
    same =  count_substring(S, L)

    #removing one character, aka type2
    delete = 0
    used = set()
    for i in range(0, s_length):
        x = S[0:i] + S[i+1:]
        if x not in used:
            delete += count_substring(x, L)
            used.add(x)

    #adding characte, aka type3
    add = 0
    used = set()
    array = ['A', 'G', 'C', 'T']
    for i in range(0, s_length + 1):
        for letter in array:
            x = S[:i] + letter + S[i:]
            if x not in used:
               used.add(x)
               add +=  count_substring(x, L)

    print(f"{same} {delete} {add}")


