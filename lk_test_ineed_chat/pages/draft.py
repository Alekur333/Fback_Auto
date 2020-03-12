from datetime import datetime

now1 = datetime.now().date()
print(now1)
current_year = str(now1.year)
print(f'Год:  {current_year}')
current_month = str(now1.month)
print(f'Месяц: {current_month}')
current_day = str(now1.day)
print(f'День:  {current_day}')