a1 = int(input("Enter thenum1 : "))
a2 = int(input("Enter thenum1 : "))
a3 = int(input("Enter thenum1 : "))
a4 = int(input("Enter thenum1 : "))

if (a1>a2 and a1>a3 and a1>a4 ):
    print("a1 is greastest ", a1)

elif (a2>a1 and a2>a3 and a2>a4):
    print("a2 is greater ",a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("a3 id the greastert : ",a3)

else:
    print("a4 id gresatr", a4)



marks1 = int(input("enter the marks : "))
marks2 = int(input("enter the marks : "))
marks3 = int(input("enter the marks : "))

total = (100*(marks1 + marks2 + marks3))/300

if (total>=40):
    print("pass")

else:
    print("fail")
