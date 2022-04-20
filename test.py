my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%x == 1)& (x%1==x) , my_list))

print(new_list)