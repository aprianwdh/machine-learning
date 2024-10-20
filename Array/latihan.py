# var_list = [1,34,1,512,34131,212,99999999999]
# left_pointer = var_list[0]

# for i in range(1,len(var_list)):
#     right_pointer = var_list[i]
#     if right_pointer > left_pointer:
#         left_pointer = right_pointer
# print(left_pointer)

# sorted_list = sorted(var_list)
# print(sorted_list[-1])

var_array = [i for i in range(101)]

for ix in var_array:
    total = sum(var_array)
    n = len(var_array)
result = total / n