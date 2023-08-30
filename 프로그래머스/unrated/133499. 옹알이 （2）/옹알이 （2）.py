def solution(babbling):
    pron = {'aya', 'ye', 'woo', 'ma'}
    count = 0
    for word in babbling:
        idx = 0
        prev = ''
        while idx <= len(word):
            if word[idx:idx+2] in pron and prev != word[idx:idx+2]:
                prev = word[idx:idx+2]
                idx += 2
                continue
            if word[idx:idx+3] in pron and prev != word[idx:idx+3]:
                prev = word[idx:idx+3]
                idx += 3
                continue
            else:
                break
        if idx == len(word):
            count += 1
    return count