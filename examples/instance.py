# Point 實體物件的設計：平面座標上的點
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def distance(self, x_target, y_target):
        return ((self.x - x_target) ** 2 + (self.y - y_target) ** 2) ** 0.5
p1 = Point(x=3, y=4)
print(p1.x, p1.y)
p1.show()
print(p1.distance(x_target=0, y_target=0))

p2 = Point(x=5, y=6)
print(p2.x, p2.y)

# FullName 實體物件的設計：分開紀錄姓、名資料的全名
class FullName:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

name_1 = FullName(first_name="H.Y.", last_name="Lai")
print(name_1.first, name_1.last)

# File 實體物件的設計：包裝檔案讀取的程式
class File:
    def __init__(self, name):
        self.name = name
        self.file = None
    def open(self):
        self.file = open(self.name, mode="r", encoding="UTF-8")
    def read(self):
        return self.file.read()
    def close(self):
        self.file.close()

f1 = File(name = "data.txt")
f1.open()
data = f1.read()
print(data)
f1.close()