country = input('請問你是台灣人還是美國人： ')
age = input('請輸入你的年齡： ')

age = int(age)

if country == '台灣':
	print('你是台灣人')
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不可以考駕照')

elif country == '美國':
	print('你是美國人')
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你還不可以考駕照')
else:
	print('國家請輸入台灣或美國')