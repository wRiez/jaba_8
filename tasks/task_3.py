money = int(input("Ваша начальная сумма: "))
procent = float(input("Процентная ставка банка: "))
years = int(input("На сколько лет кладёшь: "))

def money_(money, procent, years):
    i = 0
    while i < years:
        drop = money * procent
        money = money + drop
        i += 1
    print(f"Через {years} лет, ваша инвестиция вырастет до: {round(money, 2)}")

money_(money, procent, years)