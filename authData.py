import random
import numpy as np
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
p_number = int(input('количество паролей?'+ "\n"))
p_length = int(input('длина пароля?'+ "\n"))
l_number = int(input('количество логинов?'+ "\n"))
l_length = int(input('длина логина?'+ "\n"))

pass_arr = []
login_arr = []
for n in range(p_number):
    password =''
    for i in range(p_length):
        password += random.choice(chars)
    pass_arr.insert(n, password)
for n in range(l_number):
    login =''
    for i in range(l_length):
        login += random.choice(chars)
    login_arr.insert(n, login)
#test_data = np.concatenate((login_arr, pass_arr)) //объединение в один массив
print(f"Логины: \n {login_arr}, \n Пароли: \n {pass_arr}")
#print(test_data)