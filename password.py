#
#4. 假如說密碼錯誤 將重新詢問密碼 5.只提供3次機會密碼錯誤
#6. 假如密碼通過 將表示驗證通過 

password = "320109"
i = 3
while True:
	pwd = input("請輸入密碼:")
	if pwd == password:
		print("登入成功!")
		break
	else:
		i = i - 1
		print("密碼錯誤! 你還有",i,"次機會")
		if i == 0:
			break
