first=input('Введите любое число:')
second=input('Введите любое число:')
third=input('Введите любое число:')
if first==second and second==third:
								print('3')
elif first==second or first==third or second==third:
								print('2')
else:
								print('0')