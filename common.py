# функция, возвращающая список цифр числа, number - целое число
def digits(number):
    result = []
    number = abs(number)  # для разбора отрицательных чисел
    while number != 0:
        digit = number % 10
        result.append(int(digit))
        number = (number - digit) / 10
    result.reverse()  # при такой схеме цифры в списке будут храниться в обратном порядке
    return result

# функция, подсчитывающая количество пятерок в числе
def count_5(number):
    result = 0
    for digit in str(number):
        if digit == '5':
            result += 1
    return result
