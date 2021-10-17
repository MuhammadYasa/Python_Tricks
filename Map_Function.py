def two_squared(x):
    return x * 2

mylist = [10, 20, 30]
yourlist = []
for item in mylist:
    yourlist.append(two_squared(item))
    # the loop will add the result of the two_squared function to yourlist

print('General Programming')
print(f'mylist : {mylist}')
print(f'yourlist : {yourlist}')

print('\nPythonic')
new_list = list(map(two_squared, mylist))
print(f'new_list : {new_list}')
# map accepts 2 parameters, where each element of mylist will be raised