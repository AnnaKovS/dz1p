# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = int(input())
a1 = a // 100
a2 = a % 100 // 10
a3 = a % 10
print('Сумма цифр =', a1 + a2 + a3)


