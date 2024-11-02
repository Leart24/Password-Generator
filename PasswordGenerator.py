import random

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
password = str()

while len(password) < 14 : #password length can be changed
    if random.randint(0,1) == 0 :
        if random.randint(0,1) == 0:
            password = password + alphabet[random.randint(0,len(alphabet)-1)]
        else:
            password = password + alphabet[random.randint(0,len(alphabet)-1)].lower()
    else:
        password = password + numbers[random.randint(0,len(numbers)-1)]
print(password)
