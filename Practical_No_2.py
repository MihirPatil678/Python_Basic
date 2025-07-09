#ARITHMETIC OPERATORS
print(78+9)
print(67-8)
print(35*3)
print(32/7)
print(2**3)
print(3//2)
print(48%7)

#LOGICAL OPERATORS
print(45<55 and 20<25)
print(45<55 and 20>25)
print(45>55 and 20<25)
print(45>55 and 20>25)
print(True and True)
print(True and False)
print(False and False)
print(False and True)
print(74>26 or 78>67)
print(74>26 or 78<67)
print(74<26 or 78>67)
print(74<26 or 78<67)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(not(4>5 and 3>8))
print(not False)
print(not True)

#RELATIONAL OPERATORS
print(34>65)
print(56<87)
print(89>=89)
print(87<=98)
print(54==54)
print(56!=7)

#BITWISE OPERATORS
print(3&7)
print(3|7)
print(~3)
print(3^7)
print(3<<2)
print(3>>2)

#CONDITIONAL OPERATORS
number=-67
result="Positive" if number>0 else "Negative"
print(result)

#US DOLLAR TO INR
num=int(input('Enter The USD : '))
rupees=num*85.70
print('Rupees : ',rupees)

#BIT TO MEGABYTE,  GIGIBYTE, TERABYTE
bits=float(input('Enter The Bits : '))
MB=bits*0.000000125
GB=bits*0.000000000125
TB=bits*0.000000000000125
print(f"MB : {MB:.4f}")
print(f"GB : {GB:.4f}")
print(f"TB : {TB:.4f}")

#SQUARE ROOT
num1=float(input('Enter The Number : '))
sqrt=num1**0.5
print(f"The Square Root Of Given Number Is : {sqrt:.2f}")

#AREA OF RECTANGLE
length=float(input('Enter The Length Of The Rectangle : '))
breadth=float(input('Enter The Breath Of The Rectangle : '))
area_rectangle=length*breadth
print(f"The Area Of The Rectangle Is : {area_rectangle:.2f}")

#AREA & PERIMETER OF SQUARE
side=float(input('Enter The Length Of The Square : '))
perimeter=4*side
area_square=side**2
print(f"The Area Of The Square Is : {area_square:.2f}")
print(f"The Perimeter Of The Square Is : {perimeter:.2f}")

#TSA, CSA & VOLUME
radius=float(input('Enter The Radius Of The Cylinder : '))
height=float(input('Enter The Height Of The Cylinder : '))
CSA=2*3.14*radius*height
TSA=2*3.14*radius*(height+radius)
Volume=3.14*radius**2*height
print(f"The Curved Surface Area Of The Cylinder Is : {CSA:.2f}")
print(f"The Total Surface Area Of The Cylinder Is : {TSA:.2f}")
print(f"The Volume Of The Cylinder Is : {Volume:.2f}")

a=float(input('Enter The Value Of A : '))
b=float(input('Enter The Value Of B : '))
a,b=b,a
print(f"The Value Of A Is : {a:.2f}")
print(f"The Value Of B Is : {b:.2f}")


