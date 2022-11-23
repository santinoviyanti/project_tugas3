import datetime

y=datetime.datetime(2022, 11, 17)
print("tanggal penuggasan:" ,y)

x = datetime.datetime.now()
print("hari ini:" ,x) 

print("tahun:" ,x.year)
print("bulan:" ,x.month)
print("tanggal:" ,x.day)

print(x.strftime("%Y")) 
print(x.strftime("%B"))
print(x.strftime("%d"))
print(x.strftime("%A"))