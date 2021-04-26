# 讀取檔案
products = []
with open('products.csv', 'r') as f:
	for line in f:
		if '商品,價格' in line: 
			continue # 迴圈裡的限定功能, 如果有'商品,價格'跳到下一回, 但仍在迴圈內
		name, price = line.strip().split(',') #在 line 裡面執行去掉\n 的功能, 並在每個 ','做分割
		# 上面直接在分割後分別儲存在 name 和 price
		products.append([name, price])
print(products)

#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	# p = [name, price]
	# products.append(p)
	products.append([name, price])
print(products)

#印出所有購買紀錄
for product in products:
	print(product[0], '的價格是', product[1])

#寫入檔案
with open('products.csv', 'w') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')