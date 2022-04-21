text = 'Python Programing'

# get slice object to slice Python
sliced_text = slice(6)
print(text[sliced_text])#Pytho
#Slice ()
#rebanada (inicio, parada, paso)
#slice(start, stop, step)


py_string = 'Python'

# start = -1, stop = -4, step = -1
# contains indices -1, -2 and -3
slice_object = slice(-1, -4, -1)

print(py_string[slice_object])   # noh

py_list = ['P', 'y', 't', 'h', 'o', 'n']

# contains indices 0, 1 and 2
slice_object = slice(3)
print(py_list[slice_object]) # ['P', 'y', 't']

py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

slice_object = slice(1, 5, 2)
print(py_tuple[slice_object]) # ('y', 'h') 
