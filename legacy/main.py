from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests
import youtube_dl
import os
from pathlib import Path


def download_videos():
    dir = str(Path.home()) + os.sep + "youtube-dl-automator" + os.sep
    if not os.path.isdir(dir):
        os.makedirs(dir)
    channels = get_channels()
    get_urls(channels)


def get_channels():
    channels = []
    cwd = os.getcwd()
    filename = cwd + os.sep + "channels.txt"
    print(filename)
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            channels = f.read().split("\n")
    else:
        print("add channels.")
    return channels


def get_urls(channels):

    urls = []
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
    headers = {"User-Agent": user_agent}
    ydl_opts = {}
    n_videos = 0

    for c in channels:
        r = requests.get(c, timeout=50, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        soup = BeautifulSoup(r.content, "html.parser")

        for div in soup.findAll("div", {"class": "channel-profile"}):
            channel = div.find("span")

        dir = (
            str(Path.home())
            + os.sep
            + "youtube-dl-automator"
            + os.sep
            + str(channel)[6:-7]
        )
        if not os.path.isdir(dir):
            os.makedirs(dir)

        os.chdir(dir)

        for i, div in enumerate(
            soup.findAll("div", {"class": "pure-u-1 pure-u-md-1-4"})
        ):
            for p in div.findAll("p"):
                for a in p.findAll("a", {"title": "Audio mode"}, href=True):
                    urls.append(
                        "https://youtube.com/" + str(a["href"]).split("&", 1)[0] + "\n"
                    )
            if os.path.isfile(".last"):
                with open(".last", "r", encoding="utf-8") as f:
                    last = f.read()
                if last == urls[0]:
                    print(str(channel)[6:-7] + " hasn't uploaded new videos.")
                    urls = []
                    break
            if i == n_videos:
                with open(".last", "w", encoding="utf-8") as f:
                    f.write(urls[0])
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download(urls)
                    urls = []
                break

    return


download_videos()
