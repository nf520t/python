'''
選擇性敘述的練習-electricity
輸入何種用電和度數，計算出需繳之電費。
電力公司使用累計方式來計算電費，分工業用電及家庭用電。
                              家庭用電                工業用電
   240度(含)以下	0.15元			0.45元
   240~540(含)度   	0.25元			0.45元
   540度以上        	0.45元			0.45元
'''
(type, kwh) = eval(input('種類與度數: '))
if type == "家庭":
    if kwh <= 240:
        print(kwh * 0.15)
    elif 241 <= kwh <= 540:
        print(240*0.15 + (kwh-240)*0.25)
    else:
        print(print(240*0.15 + (540-240)*0.25) + (kwh-540)*0.45)
else:
    if kwh <= 240:
        print(kwh * 0.45)