
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?


x = 600851475143
for i in range (1,x+1):
    if x % i == 0:
        prvocislo = []
        for j in range (1,i+1):
            
            if i % j == 0:
                prvocislo.append(j)
        if len(prvocislo) == 2:
            print (i)