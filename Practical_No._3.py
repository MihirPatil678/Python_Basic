#EVEN OR ODD
num=float(input('Enter The Number : '))
if(num%2==0):
    print(num,'Is An Even Number.')
else:
    print(num,'Is An Odd Number.')

#LARGEST NUMBER
num1=float(input('Enter The First Number : '))
num2=float(input('Enter The Second Number : '))
num3=float(input('Enter The Third Number : '))
if(num1!=num2 and num1!=num3 and num2!=num3):
    if(num1>num2 and num1>num3):
        print(num1,'Is The Largest Number.')
    elif(num2>num3 and num2>num3):
        print(num2,'Is The Largest Number.')
    else:
        print(num3,'Is The Largest Number.')
else:
    print('Some Number Are Equal To Each Other.')

#LEAP YEAR OR NOT
year=int(input('Enter The Year : '))
if(year%4==0):
    print(year,'Is A Leap Year.')
else :
    print(year,'Is Not A Leap Year.')

#POSITIVE,NEGATIVE OR ZERO
number=float(input('Enter The Number : '))
if(number>0):
    print(number,'Is A Positive Number.')
elif(number<0):
    print(number,'Is A Negative Number.')
else:
    print('The Number Is Zero.')

#GRADE
marks=float(input('Enter Your Marks : '))
if(marks>=90):
    print('A Grade')
elif(marks>=80 and marks<=89):
    print('B Grade')
elif(marks>=70 and marks<=79):
    print('C Grade')
elif(marks>=60 and marks<=69):
    print('D Grade')
else:
    print('F Grade')

#SWITCH CASE USING ELSE IF LADDER
print("Select operation : ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if choice == '1':
    print("Result : ", number1 + number2)
elif choice == '2':
    print("Result : ", number1 - number2)
elif choice == '3':
    print("Result : ", number1 * number2)
elif choice == '4':
    if number2 != 0:
        print("Result : ", number1 / number2)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid input. Please choose a valid option.")







