def word_frequency():
	with open("text.txt", "r", encoding="utf-8") as file:
		text = file.read()

	text = text.lower()
	symbols = ".,!?–—:;…«»()\""

	for symbol in symbols:
		text = text.replace(symbol, "")

	words = text.split()
	frequency = {}

	for word in words:
		if word in frequency:
			frequency[word] += 1
		else:
			frequency[word] = 1

	for word, count in frequency.items():
	 	print(word, ":", count)


word_frequency()