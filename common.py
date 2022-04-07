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