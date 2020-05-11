def calup(price):
    up=(price*0.1)+price
    return up

def caldown(price):
    down=price-(price*0.1)
    return down
price= float(input("請輸入昨日收盤價"))
up = calup(price)
down = caldown(price)
print(up)
print(down)
