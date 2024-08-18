## 網路連線
import urllib.request as request
import ssl

## 現在使用 re 會走 ssl 協定，所以需要在程式中將 certification 驗證改成不需要驗證即可
ssl._create_default_https_context = ssl._create_unverified_context
# src = "https://www.lib.ncu.edu.tw/"
# with request.urlopen(src) as response:
#     data = response.read().decode("UTF-8")
# print(data)

## 串接、擷取公開資料
import json
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data = json.load(response)

company_list = data["result"]["results"]

with open("company_data.txt", mode="w", encoding="UTF-8") as file:
    for company in company_list:
        file.write(company["公司名稱"] + "," + company["統編"] + "\n")