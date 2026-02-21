#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        res = 0
        try:
            # Bölməni icra etməyə çalışırıq
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            # Sıfıra bölmə halında
            print("division by 0")
        except TypeError:
            # Element rəqəm deyilsə
            print("wrong type")
        except IndexError:
            # Siyahılardan biri çox qısadırsa
            print("out of range")
        finally:
            # Hər bir halda nəticəni (uğurlu bölmə və ya 0) siyahıya əlavə edirik
            new_list.append(res)
    return new_list
