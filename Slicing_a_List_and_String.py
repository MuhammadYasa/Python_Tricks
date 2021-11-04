print('General programming for slicing')

mylist = [10, 20, 30, 40, 50, 60]
your_list = []

for i in range(2, 5):
    your_list.append(mylist[i])
print(f'isi dari your_list : {your_list}')

print('\nPython programming for slicing')
p_list = mylist[2:5] # 2 = starting index bertipe insklusif dan end index bersifat ekslusif
# inklusif = di sertakan, ekslusif = tidak disertakan

print(f'slicing dengan python : {p_list}')

p_list_2 = mylist[2:] # end index tidak di definisikan = sampai batas akhir data

p_list_3 = mylist[:4]
# bisa juga di gunakan untuk start index di kosongkan = dari awal data
print(f'slicing with end index of data : {p_list_2}')
print(f'slicing with default start index : {p_list_3}')


print('Slicing with text')
words = 'Perkebunan'
print(words[3:-2])
# -2 berarti di mulai dar index terakhir nomor 2 sebagai batas akhir yg tidak disertakan