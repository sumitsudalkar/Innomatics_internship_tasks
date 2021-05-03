def print_formatted(n):
    alignment = len(bin(n)[2:])
    for num in range(1, n + 1):
        n_dec = str(num)
        n_oct = oct(num)[2:]
        n_hex = hex(num)[2:].upper()
        n_bin = bin(num)[2:]
        print(n_dec.rjust(alignment), n_oct.rjust(alignment), n_hex.rjust(alignment), n_bin.rjust(alignment))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
