## 參數的預設資料
def power(base=2, exp=0):
    print(base ** exp)

power(base=3)

## 使用參數名稱對應
def divide(a, b):
    print(a / b)

divide(2, 4)
divide(b=2, a=4)

## 無限(不定)參數資料
def avg(*num):
    summation = 0
    for i in num:
        summation += i
    print(summation / len(num))

avg(3, 4)
avg(3, 100, 89, -9)