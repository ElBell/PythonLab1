from datetime import datetime

counter: int = 0
year: int = 1901
month: int = 1

current: datetime = datetime(year, month, 1)

while current.year < 2001:
    if current.weekday() == 6:
        counter += 1
    if month+1 == 13:
        month = 1
        year += 1
    else:
        month += 1
    current = datetime(year, month, 1)

print(str(counter))
