# printing text in password format

txt = input('Enter a text :')
first = txt[0]
second = txt[-1]
length = len(txt)
num_stars = '*' * length
result = first + num_stars + second
print('*'* 50,'Your text is encrypted', '*' * 50)
print('*' * 50)
print('Before encryption :')
print(txt)
print('*' * 50)
print('After encryption  :')
print(result)

# printing highest number and highest digit


'''num = int(input('Enter a two  digit number :'))

str_num = str(num)
first = int(str_num[0])
last = int(str_num[1])
if (num > 25):
    print('Your number', num, 'is greater than 25')
    if (first > last):
        print('your first digit is', first, 'greater than  second digit', last)
    else:
        print('your first digit is', first, 'smaller than second digit', last)

else:
    print('Your number', num, 'is smaller than 25')
    if (first > last):
        print('your first digit is', first, 'greater than  second digit', last)
    else:
        print('your first digit is', first, 'smaller than second digit', last)

'''

