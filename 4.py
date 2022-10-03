# Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs), 
# которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict, 
# состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.

def biggest_dict(**first_one):
    my_dict = {"first_one": 'we can do it'}
    for i,j in first_one.items():
        my_dict[i] = j
    return my_dict

print(biggest_dict(first_one_1 = 1, first_one_2=2, first_one_3=True))