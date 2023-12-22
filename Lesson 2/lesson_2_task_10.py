def bank(x, y):
    interest_rate = 0.10
    
    for i in range(y):
        x += x * interest_rate

    return x

initial_deposit = 5000  
years = 7  

result = bank(initial_deposit, years)

print('Сумма на счету спустя', years, 'лет', 'составит:', result)
