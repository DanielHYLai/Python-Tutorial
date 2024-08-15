## 集合的運算
s = {3, 4, 5}

print(3 in s)  # 3 是否在集合中？ => True
print(9 in s)  # 9 是否在集合中？ => False

print(9 not in s)  # 9 是否不在集合中？ => True
print("=" * 12)

A = {3, 4, 5, 9}
B = {4, 5, 6, 7}

s = A & B  # 取得集合間的交集
print(s)

s = A | B  # 取得集合間的聯集
print(s)

s = A - B  # 取得集合間的差集 (注意是有順序性的！)
print(s)

s = B - A
print(s)

s = A ^ B  # 取得集合間的反交集
print(s)
print("=" * 12)

s = "Hello"
print(set(s))  # 將字串拆解成集合
print("H" in s)
print("=" * 12)

## 字典的運算
dic = {
    "apples": "AAA", 
    "banana": "BBB", 
    "cancel": "CCC"
}
print(dic)

dic["apples"] = "aaa"
print(dic)
print("=" * 12)

print("apples" in dic)  # 判斷名字為 apples 的 key 是否存在？ => True
print("apple" in dic)   # 判斷名字為 apple  的 key 是否存在？ => False
print("apple" in dic)   # 判斷名字為 apple  的 key 是否不存在？ => True
print("=" * 12)

del dic["apples"]  # 刪除字典中的鍵值對 (key-value pair)
print(dic)
print("=" * 12)

dic = {x: x ** 2 for x in [3, 4, 5]}  # 透過列表的資料產生字典的鍵值對
print(dic)