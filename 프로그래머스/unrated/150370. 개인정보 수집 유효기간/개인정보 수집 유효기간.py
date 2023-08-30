def convert(date, weight):
    return sum(map(lambda x, y: int(x)*y, date.split('.'), weight))

def solution(today, terms, privacies):
    weight = [12*28, 28, 1]
    today = convert(today, weight)
    terms = list(map(lambda x: x.split(), terms))
    terms_dict = {term: int(expi)*28 for term, expi in terms}
    answer = []
    for i, privacy in enumerate(privacies):
        date, term = privacy.split()
        if today - convert(date, weight) >= terms_dict[term]:
            answer.append(i+1)
            
    return answer