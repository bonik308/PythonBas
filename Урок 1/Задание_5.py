# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

a = ord(input('Введите первую букву: ').lower())
b = ord(input('Введите вторую букву: ').lower())

print(f'Позиция буквы:', a - ord("a") + 1)
print(f'Позиция буквы:', b - ord("a") + 1)
print(f'Количество букв между ними:', b - a - 1)

