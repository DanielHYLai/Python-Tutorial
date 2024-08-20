## 主程式
## 呼叫 geometry 封包
## 在後續版本的 python 中會在封包中自動加入一個 __pycache__ 的檔案，用途和 __init__.py 相同
import geometry.point as point

result = point.distance(3, 4)
print(result)

import geometry.line as line

result = line.slope(1, 1, 4, 4)
print(result)