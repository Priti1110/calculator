"""CALCULATER"""
num1=int(input("enter the digit:-"))
num2 = int(input("enter the second second:-"))
opr = input("enter the opr:-")
if opr=="+":
    print("add the value",num1+num2)
elif opr=="-":
    print("subtract the value:-",num1-num2)
elif opr == "/":
    print("divid the value", num1/num2)
elif opr == "*":
    print("multiple the value", num1 * num2)
elif opr == "%":
    print("reminder the value", num1 % num2)
else:
    print("this is not my cup of tea")