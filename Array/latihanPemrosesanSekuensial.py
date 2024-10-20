var_list = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(var_list)):
    current_element = var_list[i]
    next_indx = i + 1

    if next_indx < len(var_list):
        next_element = var_list[next_indx]
    else:
        next_element = None

    print(f"current element = {current_element}\tNext element = {next_element}\n")



sorted_list = sorted(var_list)
n = len(var_list)

if n % 2 == 1:
    median = sorted_list[n//2]
else:
    median = (sorted_list[n//2-1] + sorted_list[n//2]) / 2

print(f"Median: {median}")
print(f"Panjang var_list: {len(var_list)}")
# print(f"Nilai terakhir i: {i}")


