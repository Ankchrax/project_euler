
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.


for i in range(900,999):
    for j in range(900,999):
        num = i*j
        snum = str(num)
        rnum = snum[ : :-1]
        if snum == rnum:
          
            print(snum)
            
            
print('End')            
