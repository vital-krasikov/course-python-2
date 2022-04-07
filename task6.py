import common

num = int(input("Введите число: "))
digits_list = common.digits(num)
digits_str = ""
for i in digits_list:
    digits_str += str(i) + "+"
digits_str = digits_str[:len(digits_str)-1]  # в конце будет лишний +, удаляем

print("Сумма цифр числа - " + str(sum(digits_list)) + " (" + digits_str + ")")
