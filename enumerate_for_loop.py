nim = ['0001','0002','0003']
name = ['Bagas','Wina','Komang']
print('general programming')
for i in range(len(nim)):
    print(f'{nim[i]}--{name[i]}')


print(f'\nPythonic')
for a, data_nim in enumerate(nim):
    print(f'{data_nim}--{name[a]}')