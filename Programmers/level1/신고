def solution(id_list, report, k):
    answer = [0 for _ in id_list]
    reported_user = [[] for _ in id_list]
    
    for case in report:
        reporter, user = case.split()
        index = id_list.index(user)
        if reporter not in reported_user[index]:
            reported_user[index].append(reporter)
    
    for reporter_list in reported_user:
        if len(reporter_list) >= k:
            for reporter in reporter_list:
                index = id_list.index(reporter)
                answer[index] += 1
    return answer
