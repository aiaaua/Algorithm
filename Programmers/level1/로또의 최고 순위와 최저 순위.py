def solution(lottos, win_nums):
    zero_cnt = lottos.count(0)
    lottos = set(lottos)
    win_nums = set(win_nums)
    min_match = len(list(lottos.intersection(win_nums)))
    max_match = min_match + zero_cnt
    answer = [min(7-max_match, 6), min(7-min_match, 6)]
    return answer
