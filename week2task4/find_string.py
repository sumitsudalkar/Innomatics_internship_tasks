def count_substring(string, sub_string):
    count_sub_string = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count_sub_string += 1
    return count_sub_string


if _name_ == '_main_':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
