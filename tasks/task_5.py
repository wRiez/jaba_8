import random

common = [1, 2, 3, 4]
rare = [1, 2, 3, 4]
epic = [1, 2, 3, 4]
legendary = [1, 2, 3, 4]

c = 0
r = 0
e = 0
l = 0

result = [[], [], [], []]

def lootbox(c, r, e, l, result):
    i = 0
    j = 0
    k = 0
    while i < 20:
        chance = random.random()
        # print(chance)
        if chance <= 0.05:
            item = random.randint(0, len(legendary) - 1)
            picruteL = item + 1
            # print(f"\033[93m{legendary[item]}")
            l += 1
            result[3].append(picruteL)
        elif 0.05 < chance <= 0.1:
            item = random.randint(0, len(epic) - 1)
            picruteE = item + 1
            # print(f"\033[95m{epic[item]}")
            e += 1
            result[2].append(picruteE)
        elif 0.1 < chance <= 0.2:
            item = random.randint(0, len(rare) - 1)
            picruteR = item + 1
            # print(f"\033[94m{rare[item]}")
            r += 1
            result[1].append(picruteR)
        else:
            item = random.randint(0, len(rare) - 1)
            picruteC = item + 1
            # print(f"\033[37m{common[item]}")
            c += 1
            result[0].append(picruteC)
        i += 1
        if i == 20:
            item = random.randint(0, len(legendary) - 1)
            l += 1
            picruteL = item + 1
            # print(f"\033[93m{legendary[item]}")
            result[3].append(picruteL)
    print(f"Выпало: \n\033[37m{c} - Обычных\n\033[94m{r} - Редких\n\033[95m{e} - Эпических\n\033[93m{l} - Легендарных")
    print(f"\033[0m")
    if e > 3:
        print("Удача!")
    elif l > 1:
        print("Большая удача!")
    print(f"\033[0m")
    print("Выпавшие предметы:")
    for j in range(len(result)):
        for k in range(len(result[j])):
            if j == 0:
                print(f"\033[37m{result[j][k]} ", end='')
            elif j == 1:
                print(f"\033[94m{result[j][k]} ", end='')
            elif j == 2:
                print(f"\033[95m{result[j][k]} ", end='')
            elif j == 3:
                print(f"\033[93m{result[j][k]} ", end='')
        print(f"\033[0m")
    print('')
    print(result)


lootbox(c, r, e, l, result)