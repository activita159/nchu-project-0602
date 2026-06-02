print('helllo world')

age = int(input('請輸入年齡：'))

if age >= 18:
    print('成年')
else:
    print('未成年')

number1 = 35
number2 = 58
result = number1 + number2
print(result)

months = ['January','February','March','April','May','June','July','August','September','October','November','December']
print(months)

m1, m2, *others = months
print(m1, m2, others, sep = ';')

print(m1, m2, others, sep = '\n')

m1, m2, *others = months
print(m1, m2, others, end = '\n')
print('fuck')

def fun():
    print(m1)
    m1 = 'llllllll'


fun()

print(m1)

