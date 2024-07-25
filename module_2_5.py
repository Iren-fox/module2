def get_matrix (n, m, value) : #n - количество строк, m - количество столбцов, value - значения элементов
	matrix = [] #пустой список
	for i in range (1, n+1) :
		list_ = []
		matrix. append (list_) #добавление пустого списка в matrix
		for j in range (1, m+1) :
			list_.append (value) #добавление значений value в качестве элементов списка
	print (matrix) 
			
			
result1 = get_matrix (2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)