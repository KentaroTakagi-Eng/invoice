from bs4 import BeautifulSoup   #HTML解析
import os
import time
import requests #HTMLの読み込み

# 以下のコードを変更して、下のリンクから、Invoice SampleのPDFをDown Loadする
# https://briarpatch.co.jp/wakaruni/invoice-template/
# https://transferwise.com/us/invoice-templates/pdf#download-template
# https://www.sample.net/business/finance/invoice/
# https://www.freshbooks.com/invoice-templates/pdf

#マニュアルのPDFに入るための共通URL "manual/xxx" このXXXで取得するPDFが変わる
download_urls = []
BASE_URL = "https://sega.jp/mdmini/manual/"

#"tmp_folder"がないことを確認し、"tmp_folder"を作成する
if os.path.exists("tmp_folder") == False:
    os.mkdir("tmp_folder")

#サーバからHTML、XMLなどの情報を取得するのに使用
html = requests.get("https://sega.jp/mdmini/manual/index.html")

soup = BeautifulSoup(html.text, "lxml") #”a”タグをすべて抽出し、linksというリストを作ります。
links = soup.find_all("a")

for link in links:
    h_ref = link.get("href")

    if h_ref and ".pdf" in h_ref:
        download_urls.append(h_ref)

for download_url in download_urls:

    file_name = download_url.split("/")[-1]
    r = requests.get(BASE_URL + download_url)
    time.sleep(1)

    if r.status_code == 200:
        with open(os.path.join("tmp_folder", file_name), "wb") as f:
            f.write(r.content)