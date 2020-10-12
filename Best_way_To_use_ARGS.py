def sum_numbers(*values: int)->float:
    sum1=0
    for i in values:
        sum1+=i
    return float(sum1)
print(sum_numbers(1,2,3))
print(sum_numbers(8,20,2))
print(sum_numbers(12.5,3.147,98.1))
print(sum_numbers(1.1,2.2,5.5))
