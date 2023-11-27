def compute_penalty(logs, ctime):
    #logs = log.split(' ')
    p_cnt = 0

    for idx in range(0, len(logs)):
        if idx >= ctime:
            if logs[idx] == 'Y':
                p_cnt += 1
        else:
            if logs[idx] == 'N':
                p_cnt += 1

    return p_cnt

def find_best_closing_time(logs):
    #logs = log.split(' ')

    score = 0
    min_penalty = float('inf')
    right_time = 0

    for idx in range(len(logs)+1):
        penalty = compute_penalty(logs, idx)

        if penalty < min_penalty:
            min_penalty = penalty
            right_time = idx

    return right_time


def get_best_closing_times(log_str):
    """
        ans = []
        valid_logs = get_valid_logs(log_str)
        for log in valid_logs:
            ans.append(find_best_closing_time(log))
        return ans
    """
    log_str = log_str.replace('\n', '')
    log_arr = log_str.split(' ')
    stack = []

    v_log = []

    print(log_arr)

    for idx, ch in enumerate(log_arr):
        if ch == 'BEGIN':
            if not stack:
                stack.append(idx)
        elif ch == 'END':
            if stack and log_arr[stack[-1]] == 'BEGIN':
                v_log.append(log_arr[stack[-1]+1:idx])
                stack.pop()

    ans = []
    
    for log in v_log:
        ans.append(find_best_closing_time(log))
    return ans


print(get_best_closing_times("BEGIN Y Y END \nBEGIN N N END"))
print(get_best_closing_times("BEGIN BEGIN \nBEGIN N N BEGIN Y Y\n END N N END"))