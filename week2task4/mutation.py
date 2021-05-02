def mutate_string(string, position, character):
    chars = list(string)
    chars[position] = character
    return "".join(chars)


if _name_ == '_main_':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
