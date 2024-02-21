import datetime

current=datetime.datetime.now()
another=datetime.datetime(2023, 10, 4)
result=current-another
print("Difference beetween 2 dates in seconds:", result.total_seconds())