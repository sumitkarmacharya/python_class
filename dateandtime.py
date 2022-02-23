from datetime import datetime

#print(datetime.now())
starting="2022-5-1"
ending="2023-5-1"

starting_date = datetime.strptime(starting, "%Y-%m-%d")
ending_date= datetime.strptime(ending, "%Y-%m-%d")
print(ending_date-starting_date)