# print("Welcome to the rollercosater")
# height=int(input("Enter the height in cm"))
# if height > 120:
#     print("You can ride in rollercoaster")
# else:
#     print("sorry, you have to grow taller before you can ride")

#write program to print number is even or odd
# print("Welcome to number is even or odd")
# number=int(input("Enter the number"))

# if (number%2)==0:
#     print("The number is even")
# else:
#     print("The number is odd")


# print("Welcome to the rollercosater")
# height=int(input("Enter the height in cm"))
# if height > 120:
#     print("You can ride in rollercoaster")
#     age=int(input("Enter age"))
#     if age<12:
#         print("You have to pay $5")
#     elif age<18:
#         print("You have to pay $7")
#     else:
#         print("YOu have to pay $2")

# else:
#     print("sorry, you have to grow taller before you can ride")


#BMI calculator

# height=input("Enter height of person")
# weight=input("Enter weight of person")
# bmi=float(weight) /(float(height) **2)
# if bmi<18.5:
#     print("You are underweight")
# elif bmi<25:
#     print("You are normal")
# else:
#     print("You are overweight")


#lap year calculator
year=int(input("Enter the year"))
if year%4==0:
    if year%100==0:
        #not a leap unless special case
        if year%400==0:
            print("This is leap year")
        else:
            print("Not leap year")
    else:
        print("leap year")
else:
    print("Not leap year")
