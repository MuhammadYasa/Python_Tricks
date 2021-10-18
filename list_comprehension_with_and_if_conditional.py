ylist = [35, 75, 53, 20]
mylist = []
for item in ylist:
    if item > 40:
        mylist.append(item)
print(f'ylist : {ylist}')
print(f'mylist : {mylist}')
"""
perulangan untuk menambahkan semua data ylist ke dalam mylist
tapi dengan kondisi nilai diatas 40, yang akan di tambahkan

loop to add all ylist data to mylist
but with the condition that the value is greater than 40, which will be added
"""

print('\nPythonic')

new_list = [datas for datas in ylist if datas > 30]
print(f'new list : {new_list}')