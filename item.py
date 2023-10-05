import  random
from datetime import datetime, timedelta

lista = ["1", "2", "3", "4", "5"]

item = random.choice(lista)

print(item)

now = datetime.now()
print("Data : ", now.day,"/", now.month,"/", now.year)
