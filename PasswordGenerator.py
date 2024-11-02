import random

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = ['.',',','!','#','$','&','+','='] #more symbols could be added just make sure they are of string type in the list

def password_generator(n):
    password = str()
    while len(password) < n :
        a = random.randint(0,2)
        #randomizing the choices and the way those choices are added to the password string 
        if a == 0 :
            if random.randint(0,1) == 0:
                password = password + alphabet[random.randint(0,len(alphabet)-1)]
            else:
                password = password + alphabet[random.randint(0,len(alphabet)-1)].lower()
        elif a==1 :
            password = password + numbers[random.randint(0,len(numbers)-1)]
        else:
            password = password + symbols[random.randint(0,len(symbols)-1)]
    return password

def main():
    n = int(input("Input the number of characters you want your password to have:"))
    output = password_generator(n)
    print(output)

main()
