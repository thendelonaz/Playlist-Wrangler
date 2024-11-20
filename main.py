import colorama
from colorama import Fore
from pyfiglet import Figlet
import yt_dlp as youtube_dl
import time

colorama.init(autoreset=True)

def error_message(message):
    print(Fore.RED + f"{message}")

def success_message(message):
    print(Fore.GREEN + f"{message}")

def figlet_font(font, text):
    try:
        figlet = Figlet(font=font)
        print(Fore.CYAN + figlet.renderText(text))
    except Exception as e:
        error_message(f"Error with font '{font}': {e}")

def extract_video_urls(playlist_url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'extract_flat': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(playlist_url, download=False)
        if 'entries' in result:
            return [entry['url'] for entry in result['entries']]
        else:
            return [playlist_url]

def vid_downloader():
    try:
        yt_link = input("Paste YouTube playlist link: ")
        video_urls = extract_video_urls(yt_link)
        print(Fore.CYAN + f'NUMBER OF VIDEOS IN THE PLAYLIST: {len(video_urls)}')
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': True,
            'no_warnings': True,
            'forcefilename': True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            counter = 0
            for video_url in video_urls:
                ydl.download([video_url])
                counter += 1
                print(Fore.CYAN + f'DOWNLOADED: {counter}/{len(video_urls)}', end='\r')
        success_message("ALL Videos Downloaded successful!")
    except Exception as e:
        error_message(f"Failed to download. Error: {e}")

def Audio_downloader():
    try:
        yt_link = input("Paste YouTube playlist link: ")
        video_urls = extract_video_urls(yt_link)
        print(Fore.CYAN + f'NUMBER OF VIDEOS IN THE PLAYLIST: {len(video_urls)}')
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': True,
            'no_warnings': True,
            'forcefilename': True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            counter=0
            for video_url in video_urls:
                ydl.download([video_url])
                counter +=1
                print(Fore.CYAN + f'DOWNLOADED: {counter}/{len(video_urls)}', end='\r')
                time.sleep(0.5)
        success_message("All videos converted to Audio successfully!")
    except Exception as e:
        error_message(f"Failed to convert. Error: {e}")

def reprompt():
    while True:
        print("1. Download videos")
        print("2. Convert videos to Audio")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            vid_downloader()
            break
        elif choice == "2":
            Audio_downloader()
            break
        else:
            error_message("Invalid choice. Please select 1 or 2.")

    while True:
        more = input("Do you want to download more? (yes/no): ")
        if more.lower() in ['yes', 'y']:
            return True
        elif more.lower() in ['no', 'n']:
            return False
        else:
            error_message("Invalid response. Please enter 'yes' or 'no'.")

def main():
    figlet_font('doom', 'Welcome to the YouTube Playlist Downloader!')
    while reprompt():
        pass

if __name__ == "__main__":
    main()
