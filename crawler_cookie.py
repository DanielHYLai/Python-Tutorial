# 抓取 PTT 八卦版網頁原始碼（HTML）
import urllib.request as req
import bs4

def dataGet(url):
    # 網頁原始碼 -> Network -> index.html -> Headers -> User-Agent & Cookie
    # 如果沒有加入 Cookie 的話，data 會卡在確認是否成年的畫面，
    # 所以這邊透過傳入 Cookie 的方式來連線到 PTT 的網頁
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36", 
        "cookie": "over18=1"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("UTF-8")

    # print(data)

    # 解析原始碼，取得文章標題

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")

    for title in titles:
        if title.a != None:
            print(title.a.string)

    nextLink = root.find("a", string="‹ 上頁")  # 找到內文是 "‹ 上頁" 的 a 標籤
    # print(nextLink["href"])
    return nextLink["href"]

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
counter = 0
while counter < 5:
    url = "https://www.ptt.cc" + dataGet(url=url)
    counter += 1