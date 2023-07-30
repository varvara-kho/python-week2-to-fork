print("Hello! Welcome to the calculator.")
choice = "yes";
while (choice == "yes") :
  num1=float(input("Enter the first number:"))
  num2=float(input("Enter the second number:"))
  print("Menu:")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  num3=int(input("Choose an operation (enter the number):"))
  if num3 == 1:
    print("Result:", num1+num2)
  elif num3 == 2:
    print("Result:", num1-num2)
  elif num3 == 3:
    print("Result:", num1*num2) 
  elif num3 == 4:
    print("Result:", num1/num2)
  else:
     print("Error: Try again") 
  choice=input("Do you want to continue? (yes/no):") 
print("Thank you for using the calculator. Goodbye!")
