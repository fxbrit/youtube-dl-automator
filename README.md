# youtube-dl-automator
Script that automatically downloads youtube videos whitout you ever visiting the website, and organizes them in a convenient way.

Given a list of channel feeds, the script retrieves the xml of the channel's feeds, and then downloads the most recent video from youtube using [youtube-dl](https://youtube-dl.org/). The videos are then saved in `~/youtube-dl-automator`, each one in a directory which has the same name as the channel, in order to have a sort of ordered and directory-based library. In this way you can have automatic downloads of the latest uploads of your favourite channels without ever visiting youtube, by running the script everytime you want or by automating its execution after a given amount of time using, for example, [cron](https://man7.org/linux/man-pages/man5/crontab.5.html) or aliases.

## Why
I don't like interacting with youtube frontend, or any platform that contains invasive tracking. Simple as that.

I decided to switch to the RSS feed as invidious instances are often being blocked. The script downloads from youtube in order to get the highest quality possible on videos.

Please note that this tool should be used **behind a VPN** in order to mask your IP and prevent youtube from getting it, and then use it to track you and/or ban you (they don't like youtube-dl). You are contacting youtube servers both by fetching the feed and by downloading the video so be aware of that. However by not accessing youtube frontend you are avoiding a ton of trackers and cookies, as well as saving time and bandwidth by avoiding ads.

## How to
Clone the repository:
```
git clone https://github.com/fxbrit/youtube-dl-automator
```
then inside the directory create `feeds.txt`, and in it enter a list of urls of channel feeds, one for line with no separator. An example of `feeds.txt` can be found below:
```
https://www.youtube.com/feeds/videos.xml?channel_id=yourfavouritechannelid
https://www.youtube.com/feeds/videos.xml?channel_id=uhanothergoodchannelid
```

After this you can simply enter `python3 main.py`, just remember to install the required dependencies.
I personally like and suggets to use an **alias** such as `alias ytdl="/path/to/youtube-dl-automator/venv/bin/python3 /path/to/youtube-dl-automator/main.py`, in order to fetch manually when I know I'll watch my favourite channels.
If you want to automate the execution with **cron** enter `crontab -e` and then add a line like `* */6 * * * cd /path/to/youtube-dl-automator/ && venv/bin/python3 ./main.py`. This job for instance will check the channels every 6 hours and download the last upload in case it is new. A new video means that you haven't downloaded it using `youtube-dl-automator`: the script uses a file to keep track of the last video it downloaded for each channel in a file called `.last`, present in each channel folder.

## Troubleshooting
If a download went wrong and the script isn't able to re-download, deleting `.last` will likely fix the issue. The script itself handles it a bit better now, so it shouldn't occur, or at least not as often.

I noticed that `youtube-dl` is not really stable when used in python and it can return errors unrelated to the script or to invidious. If you notice this please consider reporting it to the youtube-dl team, I'm sure they would appreciate contributions.

## Legacy
I will no longer be scraping invidious as the downtimes were too frequent and made the script basically useless some days. I decided to leave the old script in `./legacy` in case someone wants to use it or edit it. Below I'll also include a section of the old readme, check the history of the repo for more details.

`Given a list of channels using their invidious links, the script scrapes the url of the last uploaded video on each channel, and then downloads it from youtube using youtube-dl.
I decided to scrape invidious because google doesn't like when you scrape its websites. Instead, the script downloads from youtube in order to get the highest quality possible on videos.
Issues are often caused by invidious instances which unfortunately tend to be banned by youtube, or can generally be unresponsive when under heavy load. In that case the http request will return an error and if that happens too often consider changing instance, at least temporarely.`