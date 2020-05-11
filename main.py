price= float(input("請輸入昨日收盤價"))
print("1.漲停價")
print("2.跌停價")
slect = int(input("要算漲停價還是跌停價"))
if slect == 1:
  up=(price*0.1)+price
  print(up)
elif slect == 2:
  down=price-(price*0.1)
  print(down)
else:
  print("參數無效")
