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

# функция, определяющая, есть ли среди цифр числа 5
def includes_5(number):
    for digit in str(number):
        if digit == '5':
            return True
    return False
