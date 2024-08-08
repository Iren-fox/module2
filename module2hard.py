a = int (input ('Введите число от 3 до 20: '))
if a < 3 or a > 20:
	print ('Ошибка')
	exit
else:
	pass_ = []
	for i in range (1, 21) :
		for j in range (i+1, 21):
			sum_ = i + j
			if a % sum_ == 0:
				if i != j : 
					pass_.append ([i, j]) 
			else :
				continue
	print (pass_)				