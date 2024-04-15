import random

door = list()
doors = int(input("Введите количество дверей: "))
prizes = int(input("Введите количество призов: "))
P1 = random.randint(1, doors)
P2 = random.randint(1, doors)

def chance_(doors, prizes, door):
    door = ["Пусто"] * (doors - prizes)
    i = 0
    while i < prizes:
        # door.pop(i)
        door.append("Приз")
        i += 1
    random.shuffle(door)
    print(door)
    print(f"\nИгрок 1 выбрал дверь под номером {P1}" f"\nИгрок 2 выбрал дверь под номером {P2}")
    print()

    def no():
        j = 0
        while j < 99:
            x = random.randint(1, doors)
            y = x - 1
            if (x != P1) and (x != P2) and (door[y] != "Приз"):
                print(f"За дверью {x} нет приза")
                print()
                break
            else:
                j += 1
                # print(j)

    def redo():
        o = 0
        while o < 99:
            pc = (random.randint(1, doors) - 1)
            z = pc + 1
            if (z != P1):
                print(f"Игрок 1 решает изменить свой выбор и выбирает дверь номер {z}")
                if door[pc] == "Приз":
                    print("Игрок 1 выиграл")
                else:
                    print("Игрок 1 проиграл")
                p2Res = round(1 / doors, 4)
                p1Res = round(1 - p2Res, 4)
                print(f"\nВероятность выигрыша для игрока, изменившего решение: {p1Res}"
                      f"\nВероятность выигрыша для игрока, оставшегося при своём первом выборе: {p2Res}")
                break
            else:
                o += 1

    no()
    redo()




chance_(doors, prizes, door)