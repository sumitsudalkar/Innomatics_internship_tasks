TCenLimitTheorem1.py
import math
weight=int(input())
amount=int(input())
mu=int(input())
sd=int(input())
print(round(1/2*(1+math.erf((weight-mu*amount)/(sd*math.sqrt(amount)*math.sqrt(2)))),4))
