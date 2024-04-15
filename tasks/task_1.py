import random
question = ["Ваше имя", "Где ты живёшь", "Любое число", "На какой ты планете", "42 это", "Кто твой лучший друг", "Какой сегодня день", "Ты настроил свою сеть"]
answers = ["Олег", "Дмитрий", "На Марсе", "Нептун", "Венера", "34", "62", "ответ на все вопросы", "Маргарита", "Андропов", "ДА!!", "НЕТ!!", "Символ мира", "Апокалипсис"]

k = "Компьютер"
y = "Вы"
chance = 0
i = 1
while i > 0:
    print(f"Ход {i}-й")
    print(f"{k} бросает мяч")
    chance = random.randint(0, 100)
    if chance > 30:
        print("\t Бросок, вы поймали мяч")
        print(f"\t Вопрос: {question[random.randint(0, 7)]}?")
        input("\t Ответ:")
    else:
        print("\t Бросок, вы не поймали мяч")
        print(f"\t Вопрос: {question[random.randint(0, 7)]}?")
        print("\t Ответ:", answers[random.randint(0, 13)])

    print(f"{y} бросает мяч")
    chance = random.randint(0, 100)
    if chance > 30:
        print("\t Бросок, компьютер поймал мяч")
        print(f"\t Вопрос: {question[random.randint(0, 7)]}?")
        print("\t Ответ:", answers[random.randint(0, 13)])
    else:
        print("\t Бросок, компьютер не поймал мяч")
        print(f"\t Вопрос: {question[random.randint(0, 7)]}?")
        input("\t Ответ:")
    i += 1
