def match(pattern, str):
    matches = dict()
    return _match(pattern[:], str, 0, 0, matches), matches
    
def _match(pattern, str, current_ptrn, str_start, matches):
    if current_ptrn == len(pattern):
        if str_start == len(str): 
            return True
        else: 
            return False

    print(matches)

    if pattern[current_ptrn] in matches:
        for str_end in range(str_start + 1, len(str) + 1):
            if matches[pattern[current_ptrn]] == str[str_start:str_end]:
                if _match(pattern, str, current_ptrn + 1, str_end, matches):
                    return True
    else:
        for str_end in range(str_start + 1, len(str) + 1):
            matches[pattern[current_ptrn]] = str[str_start:str_end]
            if _match(pattern, str, current_ptrn + 1, str_end, matches):
                return True
            del matches[pattern[current_ptrn]]
    
    return False


print(match('aba' , 'redbluered'))
