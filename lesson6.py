# type conversion - type casting
# print('1' + 1) -> TypeError: can only concatenate str (not "int") to str
print(int('1') + 1)  # converts string '1' to integer

print('1', type('1'))  # <class 'str'>
print(int('1'), type(int('1')))  # <class 'int'>
print(float('1'), type(float('1')))  # <class 'float'>
print(str(1), type(str(1)))  # <class 'str'>