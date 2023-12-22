
def is_year_leap(year):
    if year % 4 == 0:
         return True
    else:
        return False

result = is_year_leap(2023)

print('Год 2023:', result)