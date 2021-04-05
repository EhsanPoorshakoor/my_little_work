# hacker one 17
def minion_game(string):
    vowel = 0
    consnt = 0
    tool = len(string)
    for i in range(len(string)):
        if string[i] in "AEIOU":
            vowel += tool-i
        else:
            consnt += tool-i
    if vowel > consnt:
        print('Kevin' + " " + str(vowel))
    elif vowel < consnt:
        print('Stuart'  + " " + str(consnt))
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)