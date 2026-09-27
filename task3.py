def min_element():
	print("Введите количество элементов списка:")
	count = int(input())
	res = []

	print("Введите элементы списка:")

	for _ in range(count): 
		x = int(input())
		res.append(x)
		
	min_el = res[0]

	for n in res:
		if n < min_el:
			min_el = n

	print(f"Минимальный элемент списка: {min_el}")

	
min_element()