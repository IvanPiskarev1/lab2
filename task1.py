def fact(): 
	print("Введите положительное число:")
	var = int(input())

	if var < 0:
		print("Число должно быть неотрицательным.")
		return
	
	res = 1

	for i in range(1, var + 1):
		res *= i

	print(f"Факториал числа {var} = {res}")


fact()
		