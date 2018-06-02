# Due의 입력에 대한 확인
def due_check(due):
    tokens_length = [1, 2, 2, 4]

    due += '-0'
    due_input_list = due.split("-")
    token_number = len(due_input_list)

    print(due_input_list)
    for token in due_input_list:
        if not token.isdigit():
            print(1)
            return False
    if token_number > 4 or token_number < 2:
        print(2)
        return False
    else:
        index = len(due_input_list) - 1
        for token in due_input_list:
            if len(token) != tokens_length[index]:
                print(3)
                return False
            index -= 1
    return True


# 우선순위 입력에 대한 확인
def priority_check(priority):
    if not priority.isdigit():
        return False
    if int(priority) >= 6 or int(priority) < 1:
        return False
    return True


# 완료 여부 입력에 대한 확인
def finished_check(finished):
    if not finished == '1' or finished == '0':
        return False
    return True
