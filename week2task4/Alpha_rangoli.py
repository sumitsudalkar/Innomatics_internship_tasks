import string
alpha = string.ascii_lowercase

def print_rangoli(n):
    lines = []
    for row in range(n):
        to_print = "-".join(alpha[row:n])
        lines.append(to_print[::-1] + to_print[1:])
    width = len(lines[0])
    
    for row in range(n-1, 0, -1):
        print(lines[row].center(width, '-'))
        
    for row in range(n):
        print(lines[row].center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
