# import array

# x = array.array("i",[1,2,3,4,5,6,7])
# print(x)
# print(type(x))

var_list = [0 for i in range(10)]
print(var_list)

for i in range(10):
    var_list[i] = i

print(var_list)