num = 600851475143
prime_factor = []

def largest_prime_factor():
    global num
    _range = num**(1/2)
    for i in range(2,int(_range)):
        if(num%i==0):
            print(i)
            prime_factor.append(i)
            while(num%i==0 and num is not 0):
                print("inside loop")
                num=num/i
                print(num,i)
prime_factor.sort()
#print(prime_factor[len(prime_factor)-1])
largest_prime_factor()
