salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.05# Ежемесячный рост цен
money_capital = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for _ in range(months):
    spend *= (1 + increase)
    deficit = spend - (salary + money_capital)
    if deficit > 0:
        money_capital += deficit
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", 18783)
