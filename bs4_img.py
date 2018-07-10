import requests
import os
import time
import urllib
from requests.compat import urljoin
from bs4 import BeautifulSoup

#   画像を抽出したいURLをリストに格納
URLS = ["http://www.tano-c.net/release/tcplus-0027/",
        "http://aranmusic.net/tcslcd-0004/",
        "http://www.tano-c.net/release/tcplus-0029/"]

#   URLの個数だけ繰り返す
for i in range(len(URLS)):
    #   URLS[i]のURLをパースし変数urlに格納
    url = urllib.parse.urlparse(URLS[i])

    #   画像リストの配列 for文の最初に指定することでループを繰り返す度に格納しているデータをリセットする
    imgs = []

    #   URLSのi番目のURLを読み込みBSにてlxmlパース soup変数に格納
    soup = BeautifulSoup(requests.get(URLS[i]).content, 'lxml')

    #   ディレクトリが存在していない場合ディレクトリを作成する
    if not os.path.exists(url.hostname):
        os.mkdir(url.hostname)

    #   imgタグを取得しlink変数に格納 それぞれimgタグ内の拡張子がjpg,png,gifであるsrcタグを取得
    for link in soup.find_all("img"):
        if link.get("src").endswith(".jpg"):
            imgs.append(urljoin(URLS[i], link.get('src')))
        elif link.get("src").endswith(".png"):
            imgs.append(urljoin(URLS[i], link.get('src')))
        elif link.get("src").endswith(".gif"):
            imgs.append(urljoin(URLS[i], link.get('src')))

    #   imgsからtempに入れる
    for temp in imgs:
        re = requests.get(temp)
        time.sleep(5)

        #   変数urlのホスト名のフォルダに格納
        with open(url.hostname + '/' + temp.split('/')[-1], 'wb') as file:

            #   .contentにて画像データとして書き込む
            file.write(re.content)

    #   完了時に宣言
    print("Complete: ", URLS[i])

#   全部完了した際に宣言
print("All Complete!")
