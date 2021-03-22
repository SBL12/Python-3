#Asking a number from the user: Even Or odd



number = int(input("Enter Number to pass."))
#checking number E or O
if (number % 2) == 0:
 print ("Number is... EVEN!")
else:
  print("Number is... ODD!")




  #New Code: Write a program that takes a number and tells the user if the
#number is greater than 10, less than 10, or equal to 10. Don't
#forget to convert the string into an integer.

number2 = int(input("Enter Number another number:"))
if (number2)> 10:
    print("Number is greater than... 10!")
elif number2< 10:
    print("Number is less than 10!")
else: 
    print("Number is 10!")