## 數字運算
x = 3 + 6
print(x)
print("=" * 12)

x = 3 - 6
print(x)
print("=" * 12)

x = 3 * 6
print(x)
print("=" * 12)

x = 3 / 6  # 小數除法
print(x)
print("=" * 12)

x = 3 // 6  # 整數除法
print(x)
print("=" * 12)

x = 3 ** 6
print(x)
print("=" * 12)

x = 2 ** 0.5
print(x)
print("=" * 12)

x = 3 % 6  # 取餘數
print(x)
print("=" * 12)

x = 2 + 3
print(x)
print("=" * 12)

x = x + 1  # 遞迴運算
print(x)
print("=" * 12)

x += 1  # 等價於遞迴運算的簡便寫法
print(x)
print("=" * 12)

## 字串運算
s = "Hello"
print(s)
print("=" * 12)

s = 'Hello'
print(s)
print("=" * 12)

s = "Hell\"o"  # 加入跳脫字元 "\" 使得可以印出雙引號
print(s)
print("=" * 12)

s = "Hello" + "World"  # 字串串接
print(s)
print("=" * 12)

s = "Hello" "World"  # 另外一種可以在 python 達到字串串接的寫法，以 space 隔開
print(s)
print("=" * 12)

s = "Hello\nWorld"  # "\n" 可以讓字串換行
print(s)
print("=" * 12)  # 另外一種可以在 python 達到讓字串換行的方法，以 3 個雙引號包起來

s = """Hello
World"""
print(s)
print("=" * 12)

s = "Hello" * 3 + "Python"  # 將 Hello 複寫 3 次，再將 Python 連接起來
print(s)
print("=" * 12)

## python 會將字串做編號 (資料型態與 list 相同)，索引從 0 開始
s = "Hello"
print(s[0])   # 印出第一個字串
print(s[2])   # 印出第三個字串
print(s[-1])  # 印出最後一個字串

print(s[1:])   # 從第二個字串印到最後一個字串
print(s[:4])   # 從第一個字串印到第四個字串
print(s[1:4])  # 從第二個字串印到第三個字串 (注意索引中的尾數是不包含在內的！)
print("=" * 12)