def add(a, b):
    answer = a + b
    print(str(a) + ' + ' + str(b) + ' = ' + str(answer) + " \n ")
    
def sub(a, b):
    answer = a - b
    print(str(a) + ' - ' + str(b) + ' = ' + str(answer) + " \n ")
    
def mul(a, b):
    answer = a * b
    print(str(a) + ' * ' + str(b) + ' = ' + str(answer) + " \n ")

def div(a, b):
    answer = a / b
    print(str(a) + ' / ' + str(b) + ' = ' + str(answer) + " \n ")
    
while True:    
    print('A. Addition')
    print('B. Substraction')
    print('C. Multiplication')
    print('D. Division')
    print('E. Exit')

    choice = input('Input your choice : ')

    if choice == "a" or choice == "A":
        print('Addition')
        a = int(input('Enter first number : '))
        b = int(input('Enter sceond number : '))
        add(a, b)
    elif choice == "b" or choice == "B":
        print('Substraction')
        a = int(input('Enter first number : '))
        b = int(input('Enter sceond number : '))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print('Multiplication')
        a = int(input('Enter first number : '))
        b = int(input('Enter sceond number : '))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print('Division')
        a = int(input('Enter first number : '))
        b = int(input('Enter sceond number : '))
        div(a, b)
    elif choice == "e" or choice == "E":
        print('Program ended')
        quit()
   

