## 載入內建的 sys 模組並取得資訊
import sys

print(sys.platform)  # 顯示系統名稱
print(sys.maxsize)   # 顯示最大可儲存整數

## 建立 geometry 模組並載入使用
import my_modules.geometry as geo
print(geo.distance(1, 1, 5, 5))
print(geo.slope(1, 2, 5, 6))

## 調整搜尋模組的路徑
print(sys.path)

sys.path.append("my_modules")  # 在模組路徑列表中新增 my_modules
print(sys.path)

print(geo.distance(1, 1, 5, 5))