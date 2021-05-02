n = int(input())
my_arr = map(int, input().split())
# sorting my_arr and cunstructing list for storing it
print(sorted(list(set(my_arr)))[-2])
