# 1,2
from typing import Callable


def notebook() -> Callable[[str], None]:
    todo_list = []

    def add_todo(todo: str) -> None:
        todo_list.append(todo)

    def get_all() -> [str]:
        return todo_list

    return add_todo, get_all


add_todo, get_all = notebook()

add_todo("write homework")
add_todo("watch lesson")
tasks = get_all()
print(tasks)


# 3
def expanded_form(num: int) -> str:
    digits = list(str(num))
    length = len(digits)

    expanded = []
    for i in range(length):
        if digits[i] != '0':
            expanded.append(digits[i] + '0' * (length - i - 1))
    return ' + '.join(expanded)


print(expanded_form(12))


# 4

def decor(func):
    count: int = 0

    def inner():
        print('*' * 20)
        nonlocal count
        count += 1
        func()
        print(f'{count}')

    return inner


@decor
def func1():
    print('func1')


@decor
def func2():
    print('func2')


func1()
func1()
func2()
func1()
