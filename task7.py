import common
import math # python 3.8+ должен быть

num = int(input("Введите число: "))
digits_list = common.digits(num)
digits_str = ""
for i in digits_list:
    digits_str += str(i) + "*"
digits_str = digits_str[:len(digits_str)-1]  # в конце будет лишняя *, удаляем

print("Произведение цифр числа - " + str(math.prod(digits_list)) + " (" + digits_str + ")")