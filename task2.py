from tkinter import N


def str_to_bool(str_var):
    if(str_var == 'language'):
        py_str = True
        return py_str
    else:
        py_str = False
        return py_str
    

py_str = 'language'
print('\n----------\nInput string is: ' + py_str + '\nConverted string is: ')
print(str_to_bool(py_str))
print('---------\n')

py_str = 'not_language'
print('\n----------\nInput string is: ' + py_str + '\nConverted string is: ')
print(str_to_bool(py_str))
print('---------\n')