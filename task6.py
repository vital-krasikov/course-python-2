# функция, возвращающая список цифр числа, number - целое число
def digits(number):
    result = []
    number = abs(number)  # для разбора отрицательных чисел
    while number != 0:
        digit = number % 10
        result.append(int(digit))
        number = (number - digit) / 10
    result.reverse() # при такой схеме цифры в списке будут храниться в обратном порядке
    return result


num = int(input("Введите число: "))
digits_list = digits(num)
digits_str = ""
for i in digits_list:
    digits_str += str(i) + "+"
digits_str = digits_str[:len(digits_str)-1]  # в конце будет лишний +, удаляем

print("Сумма цифр числа - " + str(sum(digits_list)) + " (" + digits_str + ")")
