## 定義類別與屬性類別 (封裝在類別中的變數和函式)
class IO:
    supportedSrcs = ["console", "file"]

    def read(src):
        print("Read from", src)

## 使用類別
print(IO.supportedSrcs)
IO.read(src="file")