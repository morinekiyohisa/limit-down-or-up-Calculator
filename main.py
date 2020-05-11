#<------------------------------------------------------->
def calup(price):#漲停價計算函數
    up=(price*0.1)+price
    return up
#<------------------------------------------------------->
def caldown(price):#跌停價計算函數
    down=price-(price*0.1)
    return down
#<------------------------------------------------------->
price= float(input("請輸入昨日收盤價"))
up = calup(price)#調用calup
down = caldown(price)#調用caldown
print('漲停價',up)
print('跌停價',down)
#<------------------------------------------------------->