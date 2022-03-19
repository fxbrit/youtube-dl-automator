# youtube-dl-automator
Script that automatically downloads youtube videos whitout you ever visiting the website, and organizes them in a convenient way.

Given a list of channel feeds, the script retrieves the xml of the channel's feeds, and then downloads the most recent video from youtube using [youtube-dl](https://youtube-dl.org/). The videos are then saved in `~/youtube-dl-automator`, each one in a directory which has the same name as the channel.

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
- Use an **alias** such as `alias ytdl="/path/to/youtube-dl-automator/venv/bin/python3 /path/to/youtube-dl-automator/main.py`, in order to fetch manually when I know I'll watch my favourite channels.
- Automate the execution with **cron** enter `crontab -e` and then add a line like `* */6 * * * cd /path/to/youtube-dl-automator/ && venv/bin/python3 ./main.py`.
