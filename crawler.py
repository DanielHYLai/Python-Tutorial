# 抓取 ptt 電影版網頁原始碼 (HTML)
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"

# 建立一個 request 物件，附加 Headers 資訊 (讓爬蟲程式的行為比較像一般使用者)
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("UTF-8")

# print(data)

# 解析原始碼，取得文章標題
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
print(root.title)  # 抓到 title 標籤
print(root.title.string)  # 抓到 title 標籤的內文

print("-" * 20)

titles = root.find("div", class_="title")  # 找到由 div 包覆的 class="title" 標籤
print(titles)
print(titles.a.string)

print("-" * 20)

titles = root.find_all("div", class_="title")  # 找到所有由 div 包覆的 class="title" 標籤，回傳 list
# print(titles)
for title in titles:
    if title.a != None:
        print(title.a.string)