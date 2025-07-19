print("\tWelcome To My Calculator")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print("1. Addition")
print("2. Difference")
print("3. Multiplication")
print("4. Division")
op = int(input("Choose The Option From Above: "))

if(op==1) :
    print("Result: ",num1+num2)

elif (op==2) :
    print("Result: ",num1-num2)

elif(op==3) :
    print("Result: ",num1*num2)

elif(op==4) :
    print("Result: ",num1/num2)

else :
    print("Incorrect Option")