#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    i = 0
    k_list = []
    for i in range(list_length):
        try:
            j = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            j = 0
        except ZeroDivisionError:
            print("division by 0")
            j = 0
        except IndexError:
            print("out of range")
            j = 0
        finally:
            k_list.append(j)
    return k_list
