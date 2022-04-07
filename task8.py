import common

num = int(input("Введите число: "))
if common.count_5(num) > 0:
    print("Цифра 5 есть в числе")
else:
    print("Цифры 5 нет в числе")