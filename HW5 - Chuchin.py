# [1]
# Напишіть функцію, що приймає один аргумент.
# Функція має вивести на екран тип цього аргумента (для визначення типу використайте type)

def arg_type(arg1):
    print(type(arg1))
    return arg1

arg_type(11)
arg_type(8.0)
arg_type('11')
arg_type([1, 2, 3])
arg_type({1, 2, 3})
arg_type((1, 2, 3))



# [2]
# Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0 (флоатовий нуль).

def arg_type(arg1):

    if type(arg1) == float or type(arg1) == int:
        print(float(arg1))
    else:
        print (0.0)
    return arg1

arg_type(11)
arg_type(8.0)
arg_type('11')
arg_type('dffdfdf')

arg_type([1, 2, 3])
arg_type({1, 2, 3})
arg_type((1, 2, 3))



# [3]
# Напишіть функцію, що приймає два аргументи. Функція повинна
#   (a) якщо аргументи відносяться до числових типів - повернути різницю цих аргументів,
#   (b) якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
#   (c)якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
#   (d) у будь-якому іншому випадку повернути кортеж з цих аргументів

def func_two_args(arg1, arg2):
    # Условие (а)

    if type(arg1) == int and type(arg2) == int:
        print(arg1 - arg2)

    elif type(arg1) == float and type(arg2) == float:
        print(arg1 - arg2)

    elif type(arg1) == float and type(arg2) == int:
        print(arg1 - arg2)

    elif type(arg1) == int and type(arg2) == float:
        print(arg1 - arg2)

    # Условие (b)
    elif type(arg1) == str and type(arg2) == str:
        print(arg1 + arg2)

    # Условие (c)
    elif type(arg1) == str and type(arg2) == float:
        var_dict = {arg1: arg2}
        print(var_dict)

    elif type(arg1) == str and type(arg2) == int:
        var_dict = {arg1: arg2}
        print(var_dict)

    # Условие - все остальные (d)
    else:
        var_tuple = (arg1, arg2)
        print(var_tuple)

    return arg1, arg2


# Условие (а)
func_two_args(21, 11)
func_two_args(21, 11.0)
func_two_args(21.0, 11.0)
func_two_args(21.0, 11.0)

# Условие (b)
func_two_args('Привет', 'Обед')

# Условие (c)
func_two_args('Привет', 11.0)
func_two_args('Привет', 11)

# Условие (d)
func_two_args(11, [1, 2, 3])
func_two_args(11, {1, 2, 3})
func_two_args(11, (1, 2, 3))