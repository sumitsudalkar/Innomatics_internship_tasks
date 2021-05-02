def split_and_join(sentence):
    return "-".join(sentence.split())


if _name_ == '_main_':
    line = input()
    result = split_and_join(line)
    print(result)
