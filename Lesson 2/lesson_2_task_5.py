def month_to_season(month_num):
    if month_num in (1, 2, 12):
        season = 'Зима'
    elif month_num in (3, 4, 5):
        season = 'Весна'
    elif month_num in (6, 7, 8):
        season = 'Лето'
    elif month_num in (9, 10, 11):
        season = 'Осень'
    return season

month_num = 7
season = month_to_season(month_num)
print('Время года:', season)