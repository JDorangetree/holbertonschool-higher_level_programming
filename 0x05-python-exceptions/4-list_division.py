#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    z = range(0, list_length)
    new_list = list(z)
    for i in range(0, list_length):
        try:
            y = my_list_1[i]
            x = my_list_2[i]
            new_list[i] = y / x
        except TypeError:
            print("wrong type")
            new_list[i] = 0
        except ZeroDivisionError:
            print("division by 0")
            new_list[i] = 0
        except IndexError:
            new_list[i] = 0
            print("out of range")
        finally:
            pass
    return new_list
