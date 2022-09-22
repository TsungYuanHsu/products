# read file
products = []
with open('products.csv', 'r') as f:
	for line in f:
		if 'Product,Price' in line:
			continue # directly jump to next loop, meaning skip line 7 & 8 
		name, price = line.strip().split(',') # strip \n, and split string into string list [name, price]
		products.append([name, price])
print(products)

# User input
while True:
	name = input('Please input the product name: ')
	if name == 'q': # Quit
		print('Leave')
		print('-------------------------------------')
		break
	price = input('Please input product price: ')
	products.append([name, price])
print('The product and price list is shown as:', products)

# Print all products and prices
for p in products:
	print(p)
	print('The price of', p[0], 'is', p[1])

# write user input into csv
with open('products.csv', 'w') as f:
	f.write('Product,Price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')