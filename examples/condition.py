## 判斷式
if False:
    print("True: Running")
else:
    print("False: Running")
print("=" * 12)

x = input("Please enter a number:")  # 取得字串形式的使用者輸入

x = int(x)  # 將字串轉為整數型態

if x > 200:
    print(f"{x} is greater than 200.")
elif x >= 100:
    print(f"{x} is greater than 100 and smaller than 200.")
else:
    print(f"{x} is less than 100.")
print("=" * 12)

x = int(input("Please enter the number 1:"))
y = int(input("Please enter the number 2:"))
operator = input("Please choose the operation that you desier (+ - * /) :")

if operator == "+":
    print(x + y)
elif operator == "-":
    print(x - y)
elif operator == "*":
    print(x * y)
elif operator == "/":
    print(x / y)
else:
    print(f"There is no operation called '{operator}'!")