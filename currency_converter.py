print("Welcome to the Currency Converter!");
choice = "yes";
while (choice == "yes") :
    num1=float(input("Enter the amount of money: "))
    print("Choose the target currency for conversion:")
    print("1. Euro")
    print("2. Pound")
    print("3. Yen")
    num2=int(input("Choose the currency (enter the number):"))
    if  num2 == 1:
     euro = num1*0.91
     print("Result:", euro, "euro")
    elif num2 == 2:
     pound = num1*0.78
     print("Result:", pound,"pound")
    elif num2 == 3:
     yen = num1*140.79
     print("Result:", yen,"yen")
    else:
     print("Error: No such currency")
    choice = input("Do you want to perform another conversion? (yes/no)")
print("Thank you for using the Currency Converter. Goodbye!")
 
