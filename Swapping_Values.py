print("General Programming")
a = 10
b = 40
c = 70
print("before swapping")
print(f'a={a}, b={b}, c={c}')
d = a
a = b
b = c
c = d
print(f'after swapping')
print(f'a={a}, b={b}, c={c}')

print("\nPython Programming")
a, b, c = 100, 200, 300
print("before python swap")
print(f'a={a}, b={b}, c={c}')
a, b, c = b, c, a
print(f'after python swap')
print(f'a={a}, b={b}, c={c}')