maths, stats = [],[]
for each in range(5):
    m, s= map(int,input().split())
    maths.append(m)
    stats.append(s)
def b_value(x,y):
    n = len(x)
    xy =[x[each]*y[each] for each in range(n) ]
    x_square = [each**2 for each in x]
    b = (n*(sum(xy))-((sum(x)*sum(y))))/float(((n*sum(x_square))-sum(x)**2))
    return b
def ab_values(x,y):
    x_mean = sum(x)/float(len(x))    
    y_mean = sum(y)/float(len(y))
    b = b_value(x,y)
    a = y_mean - b*x_mean
    return a,b
    
a,b = ab_values(maths,stats)
print(a + b*80) 
