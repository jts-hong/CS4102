
def f(l1,l2,x):
    sum1 = 0
    for i in l1:
        sum1+=x[i]
    sum2 = 0
    for i in l2:
        sum2+=x[i]
    return sum1-sum2


a = [1, 1, 1, 2, 1, 1] 
print(f([0, 2, 4], [1, 3, 5],a))
