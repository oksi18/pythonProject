# string


"""
def find_digits(num):
    digits = []
    for str in num:
        if str.isdigit():
            digits.append(str)
    return ','.join(digits)


num = input("STR: ")
result = find_digits(num)
print(result)
"""

# 2

'''
def find_numbers(input_str):
    numbers = []
    cur_num = ""

    for num in input_str:
        if num.isdigit():
            cur_num += num
        elif cur_num:
            numbers.append(cur_num)
            cur_num = ""

    if cur_num:
        numbers.append(cur_num)

    return numbers


input_str = input("STR: ")
result = find_numbers(input_str)
print(result)
'''

# list comprehension
# 1
'''
greeting = 'Hello, world'
greeting2 = [u.upper() for u in greeting]
print(greeting2)
'''

# 2
'''
n = [str(num**2) for num in range(50) if num %2 != 0]
print(n)
'''

# function
'''
def lists(list):
    for item in list:
        print(item)
'''

'''
def max_numbers(a, b, c):

    max_num = max(a, b, c)
    return max_num


result = max_numbers(4, 7, 2)
print(result)
'''

'''
def numbers(*args):
    max_num = max(args)
    print("Max Number: ", max_num)
    min_num = min(args)
    return min_num


result = numbers(3, 23, 6, 8, 45)
print(result)
'''

'''
l = [3, 67, 23, 5, 9, 13]


def max_number(num):
    max_num = max(num)
    return max_num


result = max_number(l)
print("Max Number", result)
'''

'''
l = [3, 67, 23, 5, 9, 13]


def min_number(num):
    min_num = min(num)
    return min_num


result = min_number(l)
print("Min Number", result)
'''

'''
l = [3, 67, 23, 5, 9, 13]


def sum_number(num):
    sum_num = sum(num)
    return sum_num


result = sum_numbers(l)
print(result)
'''

'''
l = [3, 67, 23, 5, 9, 13]


def average_number(num):
    length = len(num)

    sum_num = sum(num)
    ave_num = sum_num / length
    return ave_num


result = average_number(l)
print(f'Average: {result}')
'''
list_ = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
status = True


def table():
    row = 1
    while row <= 10:
        column = 1
        while column <= 10:
            product = row * column
            print(product, end="\t")
            column += 1
        print()
        row += 1


while status:
    print('Menu')
    action = int(input('Enter action: '))

    match action:
        case 1:
            print(f"Min Number {min(list_)}")
        case 2:
            print(f"Without Duplicate: {set(list_)}")
        case 3:
            for i in range(len(list_)):
                if (i + 1) % 4 == 0:
                    list_[i] = 'X'
        case 4:
            for i in range(10):
                for j in range(10):
                    if i == 0 or i == 10 - 1 or j == 0 or j == 10 - 1:
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
                print(i)
        case 5:
            table()
        case 6:
            status = False
            print('Exit')
        case _:
            print('Actiond undefine')