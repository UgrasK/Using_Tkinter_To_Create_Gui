# define unlimited arguments on function with *args (args can be any name like *numbers, *letters etc.)
def add(*args):
    sum_num = 0
    for num in args:
        sum_num += num
    return sum_num


print(add(3, 5, 6, 8))
