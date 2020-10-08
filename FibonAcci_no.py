#Fibonacci No we have to print
def find_fibonacci(n):
    last, second_last = 1, 0
    if 0<=n<=1:
        return n
    sum1 = None
    for value in range(n-1):
        sum1= last + second_last
        second_last=last
        last= sum1
    return sum1
n=int(input("Enter the range you want a fibonacci series......."))
for index in range(n):
    print(index,find_fibonacci(index))
