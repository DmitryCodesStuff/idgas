ex_list = ['24', '13', '45', '23', '56', '44', '87']

sum = 0

for i in ex_list:
    if int(i) > 30:
        sum += int(i)

if sum > 200:
    remainder = sum%3
    print(f'Greater than 200, the remainder is: {remainder}')
else:
    print(f'Less than 200, the sum is: {sum}')