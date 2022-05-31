#10) Write a program that asks the user for a large integer and inserts commas into it according to the standard American convention for commas in large numbers. Forinstanc ,if the user enters 1000000, the output should be1,000,000
num=int(input('enter the value '))
print("{:,}".format(num))
