def reverse_number(x):
    num = str(x)
    rev = num[::-1]
    x = int(rev)
    print(x)
def is_palidrom(y):
    num = str(y)
    rev = num[::-1]
    polid = int(rev)
    if polid == y:
        print(f"Число {y} является полидромом")
    else:
        print(f"Число {y} не является полидромом")
def process_numbers(z):
    indx = 0
    for i in z:
        num = str(i)
        rev = num[::-1]
        polid = int(rev)
        if i == polid:
            print(f"Число {i} в списке - полидром")
            continue
        z.remove(i)
        z.insert(indx, polid)
        indx += 1
    print(z)

x = int(input("Первое число: "))
y = int(input("Второе число: "))
z = []
print("Список: ")
for i in range(11):
    k = int(input())
    z.append(k)

reverse_number(x)
is_palidrom(y)
process_numbers(z)