def fibonacci_numbers():
	print("Список чисел Фибоначчи:")
	res = [0, 1]

	while len(res) < 20: 
	    fib = res[-1] + res[-2] 
	    res.append(fib)

	print(f"Первые 20 чисел Фибоначчи: {res}")


fibonacci_numbers()
