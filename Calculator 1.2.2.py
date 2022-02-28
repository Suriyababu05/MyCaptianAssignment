print("Select the Operations to be Performed\n1.Addition \n2.Subraction\n3.Multiplication\n4.Division\n ")
while True:
    op=int(input("Enter Your Choice from 1,2,3,4 :"))
    a=int(input("Enter the first value : "))
    b=int(input("Enter the second value : "))
    if op==1:
        c=a+b
        print("Addition")
        print(a,"+",b,"=",c)
    elif op==2:
        c=a-b
        print("Subraction")
        print(a,"-",b,"=",c)
    elif op==3:
        c=a*b
        print("Multiplication")
        print(a,"*",b,"=",c)
    elif op==4:
         c=a/b
         print("Division")
         print(a,"/",b,"=",c)
    else:
          print("Invalid Option")
    print("Let's do next calculation?\n1.Yes\n2.No ")      
    next_calculation = input()
    if next_calculation == "2":
        break
   
