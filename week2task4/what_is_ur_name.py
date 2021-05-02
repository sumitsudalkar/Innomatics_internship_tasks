def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a, b))


if _name_ == '_main_':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
