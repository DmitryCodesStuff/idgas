ex_list = ['24', '13', '45', '23', '56', '44', '87']

def calculate_sum(ex_list):
    sum = 0
    for i in ex_list:
        if int(i) > 30:
            sum += int(i)
    return sum

def calculate_remainder(sum):
    remainder = sum%3
    return remainder

if __name__ == '__main__':
    sum = calculate_sum(ex_list)
    remainder = calculate_remainder(sum)
    if sum > 200:
        print(f'Greater than 200, the remainder is: {remainder}')
    else:
        print(f'Less than 200, the sum is: {sum}')