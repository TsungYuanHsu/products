# This is an expense recorder

import os #operating system

# read file
def read_file(filename):
	products = []
	with open(filename, 'r') as f:
		for line in f:
			if 'This is my purchase record' in line:
				continue # directly jump to next loop
			elif 'Product,Price' in line:
				continue # directly jump to next loop
			name, price = line.strip().split(',') # strip \n, and split string into string list [name, price]
			products.append([name, price])
	return products # save result for further use

# User input
def user_input(products):
	while True:
		name = input('Please input the product name: ')
		if name == 'q': # Quit
			print('Leave')
			print('-------------------------------------')
			break
		price = input('Please input product price: ')
		products.append([name, price])
	print('The product and price list is shown as:', products)
	return products

# Print all products and prices
def print_products(products):
	for p in products:
		print(p)
		print('The price of', p[0], 'is', p[1])

# write user input into csv
def write_file(filename, products):
	with open(filename, 'w') as f:
		f.write('This is my purchase record\n')
		f.write('Product,Price\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')


def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # Check if the csv file exists or not # filename usually is parameter
		print('File exists and found!')
		products = read_file(filename)
	else:
		print('File is not found!')
		products = []
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()