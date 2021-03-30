from __future__ import unicode_literals
import requests
import xml.etree.ElementTree as ET
import youtube_dl
import os
from pathlib import Path


def get_feeds():

    rss_feeds = []
    channels = []
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
    headers = {"User-Agent": user_agent}
    w3 = "{http://www.w3.org/2005/Atom}"
    cwd = os.getcwd()
    filename = cwd + os.sep + "feeds.txt"

    with open(filename, "r") as f:
        rss_feeds = f.read().split("\n")

    for r in rss_feeds:
        channel = {"name": "", "latest_upload": "", "uploads": []}
        r = requests.get(r, timeout=50, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        root = ET.fromstring(r.content)
        i = 0
        for c in root.iter():
            if (c.tag == w3 + "name") and (i == 2):
                channel["name"] = c.text
            if c.tag == w3 + "link":
                i += 1
                if i == 3:
                    channel["latest_upload"] = c.attrib["href"]
                elif i > 3:
                    channel["uploads"].append(c.attrib["href"])
        channels.append(channel)

    return channels


def download(channels):

    ydl_opts = {}

    for c in channels:

        dir = str(Path.home()) + os.sep + "youtube-dl-automator" + os.sep + c["name"]
        if not os.path.isdir(dir):
            os.makedirs(dir)
        os.chdir(dir)

        if os.path.isfile(".last"):
            with open(".last", "r", encoding="utf-8") as f:
                last = f.read()
            if last == c["latest_upload"]:
                print(c["name"] + " hasn't uploaded new videos.")
                continue

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([c["latest_upload"]])
            with open(".last", "w", encoding="utf-8") as f:
                f.write(c["latest_upload"])
        except Exception as e:
            print(e)


download(get_feeds())