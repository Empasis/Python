money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
i = spend - salary
month = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while i <= money_capital :
    month += 1
    spend += spend * increase
    i += spend - salary
print("Количество месяцев, которое можно протянуть без долгов:", month)
