def swap_case(s):
    res = '';
    for char in s:
        if(char.isupper()==True):
            res += (char.lower());
        elif(char.islower()==True):
            res += (char.upper());
        else:
            res += char;
    return res;
# sWAP cASE in Python - HackerRank Solution END

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
