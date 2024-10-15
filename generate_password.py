import random
import string

def gen_pass(l, words, up, numb, spec, rechar):
    str1 = ""
    password = ""
    if words:
        str1 += string.ascii_lowercase
    if up:
        str1 += string.ascii_uppercase
    if numb:
        str1 += string.digits
    if spec:
        str1 += string.punctuation
    if rechar:
        str1 = str1.replace('i', '1').replace('f', '4').replace('o', '0')
    if len(str1) == 0:
        return 1
    else:
        for y in range(l):
            password += random.choice(str1)
        return password

count = int(input("Сколько паролей необходимо? "))
l = int(input("Какова длина пароля? "))
words = input("Использовать латинские буквы в нижнем регистре? ").lower() == 'да'
up = input("Использовать латинские буквы в верхнем регистре? ").lower() == 'да'
numb = input("Использовать цифры? ").lower() == 'да'
spec = input("Использовать специмволы? ").lower() == 'да'
rechar = input("Заменить некоторые буквы на цифры? ").lower() == 'да'
print("Ваши пароли:")

for i in range(count):
    if (gen_pass(l, words, up, numb, spec, rechar) == 1):
        print("Вот ваш самый надежный пароль из ничего: qwerty")
        break
    else:
        print(gen_pass(l, words, up, numb, spec, rechar))



