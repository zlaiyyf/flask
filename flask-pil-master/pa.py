
import requests
from bs4 import BeautifulSoup



def spider(name):
    headers={
        "Host": "66.linziapp.applinzi.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "21",
        "Origin": "null",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
                "contentType":"text/html; charset=utf-8"
    }
    data={
        "a1":name
    }

    rep=requests.post(url="http://66.linziapp.applinzi.com/ye/laji.php",headers=headers,data=data)
    html = rep.text.encode("ISO-8859-1")
    html = html.decode("utf-8")
    soup = BeautifulSoup(html, 'lxml')
    # print(html)
    if soup.find("h3"):
        return soup.find("h3").text
    else:
        return "未找到分类 已记录到数据库"
    # print(soup.find("h3").text)
if __name__ == "__main__":
    # 已记录到数据库
    print(spider("cscs"))
    # print("鱼头")
# http://66.linziapp.applinzi.com/ye/laji.php