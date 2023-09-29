while int or float:
	try:
		number = float(input("what is x "))
		number2 = float(input("what is y "))
		opereter = input("+ * / - ")
		if opereter == "+":
			print(number + number2)
		elif opereter == "*":
			print(number * number2)
		elif opereter == "/":
			print(number / number2)
		elif opereter == "-":
			print(number - number2)
	except ValueError:
		print("plz enter a number")
