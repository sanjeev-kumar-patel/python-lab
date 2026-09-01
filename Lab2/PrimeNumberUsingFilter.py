def primeNo(n):
    for i in range(2,n) :
        if(n < 2):
            return False
        for i in range(2,n):
            if(n % i == 0) :
                return False
        return True
num = [x for x in range(1,101)]
prime = list(filter(primeNo,num))
print(prime)
    
    