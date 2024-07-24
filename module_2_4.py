numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers :
	is_prime = True
	for j in range (2, i) :
		
		if i % j == 0 and  i != j :
			is_prime = False
			not_primes.append (i)
			break
		else :
			is_prime = True
			
	if is_prime == True and i != 1:
		primes.append (i)
			
print ('Простые числа: ', primes)
print ('Не простые числа: ', not_primes)
				
			
	