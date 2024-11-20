# Playlist Wrangler
#### Video Demo:  <https://youtu.be/CVCza9kUWo8>

# Description

This Python script allows you to download videos or convert them to audio from a YouTube playlist. It uses the `yt_dlp` library for downloading and `colorama` for colored terminal output. Additionally, it uses `pyfiglet` to display stylized text.

## Motivation 
There are many Youtube video downloaders out there but non of them were able to solve the problem I had trying to download multiple vintage songs for my dad at once hussle free. I took it to myself to code Playlist Wrangler a software that can download full YouTube playlists in video or audio format so i can save time. It took me some time getting to understand how the `yt_dlp` library worked but I was always motivated because once I was done my dad could create playlist of his favourite songs then can download them in a matter of minutes.


## Features

- Download all videos from a YouTube playlist.
- Convert all videos from a YouTube playlist to audio files.
- Display messages in different colors for errors and success.
- Display stylized text using `pyfiglet`.

## Requirements

- Python 3.x
- `colorama` library
- `pyfiglet` library
- `yt_dlp` library
- `time` library

## Installation

1. Clone the repository or download the script.
2. Install the required libraries:

```bash
pip install colorama pyfiglet yt_dlp
