# Оператор if
x = 10
if x > 0:
    print("x - положительное число")

# Оператор else
x = -5
if x > 0:
    print("x - положительное число")
else:
    print("x - не положительное число")

# Оператор elif
x = 0
if x > 0:
    print("x - положительное число")
elif x < 0:
    print("x - отрицательное число")
else:
    print("x равно нулю")

# Цикл for с функцией range()
for i in range(5):
    print(i)

# Цикл while
i = 0
while i < 5:
    print(i)
    i += 1

# Управление циклами: break и continue
for i in range(10):
    if i == 3:
        continue  # пропускаем 3
    if i == 7:
        break  # прерываем цикл на 7
    print(i)

# Использование функции enumerate()
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)
g = input();
















