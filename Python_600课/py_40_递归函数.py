def sum_number(num):
    print(num)
    if num ==1:
        return
    sum_number(num - 1)
sum_number(3)

def sum_numbers(num):

    if num == 1:
        return 1
    temp = sum_numbers(num - 1)
    return num + temp
result = sum_numbers(998)
print(result)