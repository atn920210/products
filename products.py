import os #operating system 作業系統
# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r') as f:
		for line in f:
			if '商品,價格' in line: 
				continue # 迴圈裡的限定功能, 如果有'商品,價格'跳到下一回, 但仍在迴圈內
			name, price = line.strip().split(',') #在 line 裡面執行去掉\n 的功能, 並在每個 ','做分割
			# 上面直接在分割後分別儲存在 name 和 price
			products.append([name, price])
	print(products)
	return products
	
#讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		price = int(price)
		# p = [name, price]
		# products.append(p)
		products.append([name, price])
	print(products)
	return products

#印出所有購買紀錄
def print_products(products):
	for product in products:
		print(product[0], '的價格是', product[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')
#檢查檔案是否存在
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('yeah! 找到檔案了!')
		products = read_file(filename)
	else:
		print('找不到檔案...')

	user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()