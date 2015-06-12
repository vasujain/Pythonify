import lib701

def Move(label):
    label = "Anything"

def Use(label):
    label[1] = ":^)"
    

a_list = [1, 2, 3]

lib701.Move(a_list)
print(a_list)
# [1, 2, 3]

lib701.Use(a_list)
print(a_list)
# [1, ':^)', 3]

a_tuple = (4, 5, 6)
lib701.Move(a_tuple)
print a_tuple
# (4, 5, 6)

lib701.Use(a_tuple)
# TypeError: 'tuple' object does not support item assignment
print lib701.Use(a_tuple)
# TypeError: 'tuple' object does not support item assignment

a_string = "bird"
lib701.Move(a_string)
a_string
# 'bird'

lib701.Use(a_string)
#TypeError: 'str' object does not support item assignment

a_number = 3
lib701.Move(a_number)
print a_number
# 3

lib701.Use(a_number)
#TypeError: 'int' object does not support item assignment
