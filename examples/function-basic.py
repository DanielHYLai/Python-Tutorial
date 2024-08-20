## 定義函式

## 函式的程式碼，若是沒有被呼叫，就不會執行
def multiply():
    print(3 * 4)

def multiply_1(n1, n2):
    print(n1 * n2)

def multiply_2(n1, n2):
    print(n1 * n2)
    
    return 100

## 如果函式會有額外的操作需要將資料儲存於變數，可以考慮使用 return，而非直接印出來
def multiply_3(n1, n2):
    return n1 * n2

## 呼叫函式
multiply()
multiply_1(10, 12)

value = multiply_1(10, 12)
print(value)  # 沒有指定 return 的資料就會回傳 None

value = multiply_2(10, 12)
print(value)

value = multiply_3(1, 2) + multiply_3(4, 10)
print(value)

## 程式的包裝: 同樣的程式可以重複運用
def cumSum(num):
    n = 0
    for i in range(1, num + 1):
        n += i
    print(n)

cumSum(10)
cumSum(100)