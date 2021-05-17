import math
weight=int(input())
amount=int(input())
m=int(input())
s=int(input())
print(round(1/2*(1+math.erf((weight-m*amount)/(s*math.sqrt(amount)*math.sqrt(2)))),4))
