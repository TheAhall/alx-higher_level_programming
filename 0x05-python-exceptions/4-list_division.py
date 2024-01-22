#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    quotient = 0
    for i in range(0, list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            quotient = 0
            print("division by 0")
        except TypeError:
            quotient = 0
            print("wrong type")
        except IndexError:
            quotient = 0
            print("out of range")
        finally:
            pass
        new_list.append(quotient)
    return new_list
