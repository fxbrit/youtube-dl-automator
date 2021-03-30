# youtube-dl-automator
Script that automatically downloads youtube videos whitout you ever visiting the website, and organizes them in a convenient way.

Given a list of channels using their [invidious](https://redirect.invidious.io/) links, the script scrapes the url of the last uploaded video on each channel, and then downloads it from youtube using [youtube-dl](https://youtube-dl.org/). The videos are then saved in `~/youtube-dl-automator`, each one in a directory which has the same name as the channel, in order to have a kind of ordered library. In this way you can have automatic downloads of the latest uploads of your favourite channels without ever visiting youtube, by running the script everytime you want or by automating its execution after a given amount of time using, for example, [cron](https://man7.org/linux/man-pages/man5/crontab.5.html). 

## Why
I don't like interacting with youtube, or any platform that contains invasive tracking. Simple as that.

I decided to scrape invidious because google doesn't like when you scrape its websites. Please note that this tool should be used **behind a VPN** in order to mask your IP and prevent youtube from getting your IP, and then use it to track you and/or ban you (they don't like youtube-dl).
Instead, the script downloads from youtube in order to get the highest quality possible on videos.

## How to
Clone the repository:
```
git clone https://github.com/fxbrit/youtube-dl-automator
```
then inside the directory create `channels.txt`, and in it enter a list of urls of invidious channels, one for line with no separator. An example of `channels.txt` can be found below:
```
invidious.xyz/channel/yourfavouritechannel
invidious.xyz/channel/uhanothergoodchannel
```

After this you can simply enter `python3 main.py`, just remember to install the required dependencies.
If you want to automate the execution enter `crontab -e` and then add a line like `* */6 * * * /usr/bin/python3 /path/to/youtube-dl-automator/main.py`. This line for instance will check the channels every 6 hours and download the last upload in case it is new (new means that you haven't downloaded it using `youtube-dl-automator`, the script uses a file to keep track of it).

#### Tweaks
Currently the script is set to check only for the last upload. You can change this in the source code if you wish to download or check for more videos at the same time. For example this could be useful if you want to download the last 20 uploads of a channel the first time you add it to your channels file.

Also, as I previously stated, the last uploaded is tracked by using files to store, for each channel, which was the most recent downloaded upload. This is fairly primitive and it might be problematic if something goes wrong during a download. In case of issues `cd` to the channel directory and then `rm .last`.
Please also notice that even if you increase the number of downloads to a large number if `youtube-dl-automator` detects that you have download the most recent video it will not go on as it assumes you already watched everything up to the most recent video you downloaded.

## Troubleshooting
Issues are often caused by invidious instances which unfortunately tend to be banned by youtube, or can generally be unresponsive when under heavy load. In that case the http request will return an error and if that happens too often consider changing instance, at least temporarely.

The script can have problems when a download goes wrong and it started fetching a video without finishing, as it will remember the video as downloaded even if it was not. I will change the way this is handled at some point as I fair it will lead to other issues.

Additionally I noticed that `youtube-dl` is not really stable when used in python and it can return errors unrelated to the script or to invidious. If you notice this please consider reporting it to the youtube-dl team, I'm sure they would appreciate contributions.