a=int(input())
b=int(input())
m=int(input())
prob = 1;
for i in range(b):
    prob*=a
print(prob)
print(prob%m)
