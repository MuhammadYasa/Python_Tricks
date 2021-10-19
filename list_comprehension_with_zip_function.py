name = ['bedjo', 'kartil', 'sutejo']
age = [30, 22, 35]
mylist = []
for i in range(len(name)):
    mylist.append([name[i], age[i]])
print('general programming')
print(f'mylist : {mylist}')

print('\nPythonic')
new_list = [[d_name, d_age] for d_name, d_age in zip(name, age)]
print(f'new list : {new_list}')