nim = ['0001','0002','0003']
name = ['Bagas','Wina','Komang']

print('general programming')
for z, data_name in enumerate(name):
    print(f'{nim[z]}--{data_name}')


print('\nPythonic')
for d_nim, d_name in zip(nim,name):
    print(f'{d_nim}--{d_name}')

print('\nwith 3 value')
hobby = ['play', 'photo', 'sleep']

for a_nim, a_name, a_hobby in zip(nim, name, hobby):
    print(f'{a_nim}--{a_name}--{a_hobby}')