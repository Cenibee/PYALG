'''
영어 끝말잇기
1 -> 2 -> 3 -> ... -> 1
단어 중복 불가
두 글자 이상

'''

def solution(n, words):
    checker = set()
    last_word = ''
    ends_turn = -1
    for turn, word in enumerate(words):
        if word in checker or\
            last_word and last_word[-1] != word[0]:
                ends_turn = turn
                break
        checker.add(word)
        last_word = word

    if ends_turn == -1: return (0 , 0)
    turn, player = divmod(ends_turn, n)
    return [player + 1, turn + 1]

print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))