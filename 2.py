num1 = input()
while num1.isdigit() != True:
    num1 = input("Введите число")
num1 = int(num1)

a = input()
while a != '+' and a != '-' and a != '*' and a != '/':
    a = input("Введите один из следующих операторов: +, -, *, /")

num2 = input()
while num2.isdigit() != True:
    num2 = input("Введите число")
num2 = int(num2)

if a == '+':
    result = num1 + num2
elif a == '-':
    result = num1 - num2
elif a == '*':
    result = num1 * num2
elif a == '/' and num2 == 0:
    result = "На ноль делить нельзя"
elif a == '/' and num2 != 0:
    result = num1 // num2


print(result)
