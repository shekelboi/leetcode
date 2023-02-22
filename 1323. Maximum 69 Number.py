def maximum69Number(num: int) -> int:
    n_string = str(num)
    for i in range(len(n_string)):
        if n_string[i] == '6':
            n_string = n_string[:i] + '9' + n_string[i + 1:]
            break
    return int(n_string)