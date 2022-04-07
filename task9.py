import common

num = int(input("Введите число: "))

max_digit = 0
for i in common.digits(num):
    if i > max_digit:
        max_digit = i

print("Цифра " + str(max_digit) + " - максимальная в числе " + str(num))