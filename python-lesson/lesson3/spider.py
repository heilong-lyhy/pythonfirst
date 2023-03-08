import urllib.request#导入url-lib-request模块
import re #导入re正则库

#设置网址
def download_html(url):
  #http头信息
  header = {
  "搞不懂，先空着"
  }

  #构造一个request请求对象
  req =urllib.request.Request(url=url,headers=header)

  #向网站服务器发送请求，获取到回复response
  response = urllib.request.urlopen(req)

  #读取回复并使用UTF-8编码进行解码
  html = response.read().decode("utf-8")

  return html

def extract_url(html):
  pattern ="https://www.bilibili.com"

  urls =re.findall(pattern,html)

  return set(urls)

file = open("XX.txt","r")
output = open ("movie.txt","w")

lines = file.readlines()

for url in lines:

  url = url.strip()
  print(url)
  
  html = download_html(url)

  urls = extract_url(html)
  for url in urls:
    output.write(url + '\n')


file.close()
output.close()

