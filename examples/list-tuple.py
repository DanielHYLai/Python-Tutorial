## list tutorial
grades = [12, 60, 70, 15, 90]
print(grades)
print("=" * 12)

print(grades[0])
print(grades[4])
print(grades[1:4])
print("=" * 12)

grades[0] = 55  # 將列表第一個元素改為 55
print(grades)
print("=" * 12)

grades[1:4] = []  # 將列表中第二個元素到第四個元素移除
print(grades)
print("=" * 12)

grades = grades + [100, 99, 88]  # 將列表做串接
print(grades)
print("=" * 12)

length = len(grades)  # 取得列表的長度 (元素個數)
print(length)
print("=" * 12)

## 建構巢狀列表 (nested list)
data = [
    [1, 2, 3], 
    [4, 5, 6]
]
print(data)
print(data[0])  # 印出第一層的列表
print(data[1])  # 印出第二層的列表
print(data[1][0])  # 印出第二層列表的第一個元素
print(data[0][2])  # 印出第一層列表的第三個元素

data[0][0:2] = [1, 2, 3, 4]  # 將第一層列表的第一個到第二個元素替換成指定資料
print(data)
print("=" * 12)

## tuple tutorial
data = (3, 4, 5)
print(data[0:2])

## tuple 中的元素是不可變動的，因此以下的程式碼會發生錯誤
try:
    data[0] = 100
except TypeError as e:
    print(e)