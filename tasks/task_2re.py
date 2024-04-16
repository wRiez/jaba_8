def reverse_number(x):
    num = str(x)
    rev = num[::-1]
    x = int(rev)
    print(x)
    return x
def is_palidrom(y):
    x = reverse_number(y)
    if y == x:
        print(f"Число {y} является полидромом")
    else:
        print(f"Число {y} не является полидромом")
    return x
def process_numbers(z):
    indx = 0
    for i in z:
        w = is_palidrom(i)
        z.remove(i)
        z.insert(indx, w)
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