products = []
while True:
	name = input('Please input the product name: ')
	if name == 'q': # Quit
		print('Leave')
		print('-------------------------------------')
		break
	price = input('Please input product price: ')
	products.append([name, price])
print('The product and price list is shown as:', products)

for p in products:
	print(p)
	print('The price of', p[0], 'is', p[1])