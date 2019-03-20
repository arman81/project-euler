limit = int(4*1e6)
print(limit)
result = []
def fib_even_sum():
    a = 1
    b = 2
    result.append(1)
    while(b<limit):
        result.append(b)
        print(a,',',b)
        temp = b
        b = a+b
        a = temp
fib_even_sum()
s = [i for i in result if(i%2==0)]
print(s)
print(sum(s))
