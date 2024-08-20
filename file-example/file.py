# ## 儲存檔案
# ## method 1: 一般寫法需要加上 close()
# file = open("data.txt", mode="w", encoding="UTF-8")
# file.write("Hello World!\nHello File!\n測試中文")
# file.close()

# ## method 2: 使用 with 會自動關閉檔案
# with open("data_write.txt", mode="w", encoding="UTF-8") as file:
#     file.write("Hello World!\nHello File!\n測試中文")

# with open("number_list.txt", mode="w", encoding="UTF-8") as file:
#     file.write("3\n4\n5")

# ## 寫入檔案
# with open("data_write.txt", mode="r", encoding="UTF-8") as file:
#     data = file.read()
# print(data)

# n = 0
# with open("number_list.txt", mode="r", encoding="UTF-8") as file:
#     for data in file:
#         n += int(data)
# print(n)

## 使用 JSON 格式寫入＆讀取檔案
import json

with open("config.json", mode="r") as file:
    data = json.load(file)
print("Full File:", data)
print("Name:", data["name"])
print("Version:", data["version"])

data["version"] = "1.2.6"

with open("config.json", mode="w") as file:
    json.dump(data, file)