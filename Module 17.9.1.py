def lst_sort(lst):
     return sorted(lst)
def lst_find_num(lst, num):
     for i in range(len(lst) - 1):
         if num > lst[i] and num <= lst[i + 1]:
            return i + 1
     return -1

def f():
        try:
            seq = list(map(int, input('Введите числа через пробел: ').split()))
            num = int(input('Введите любое число: '))
            seq_sorted = lst_sort(seq)
            position = lst_find_num(seq_sorted, num)
            print('Сортированный по возрастанию список:', *seq_sorted)
            print('Позиция в списке', *seq_sorted, 'для числа', num, 'является', position)
        except ValueError:
                print("Для ввода доступны только числа, попробуйте заного")
try:
    f()
except UnboundLocalError:
    print()