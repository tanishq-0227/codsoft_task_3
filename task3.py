import random
import string
print("Welcome to the Random Password Generator.")
print("-----------------------------------------")

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

letters=lower+upper

n_letters=int(input("How many letters you want in your password?\n"))
n_digits=int(input("How many digits you want in your password?\n"))
n_symbols=int(input("How many symbols you want in your password?\n"))

pass_list=[]

for i in range(1,n_letters+1):
    char=random.choice(letters)
    pass_list += char

for i in range(1,n_digits+1):
    char = random.choice(digits)
    pass_list += char

for i in range (1,n_symbols+1):
    char = random.choice(symbols)
    pass_list += char

random.shuffle(pass_list)

password=""
for char in pass_list:
    password += char
print("So here is your strong password:\n",password)