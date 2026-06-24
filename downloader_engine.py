import os
import sys
from yt_dlp import YoutubeDL

# Silence the standard tech clutter
class MyQuietLogger:
    def debug(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): print(msg)

last_percent = None

# Custom hook specifically optimized for the Windows terminal display
def my_hook(d):
    global last_percent
    if d['status'] == 'downloading':
        percent_str = d.get('_percent_str', '0').replace('%', '').strip()
        try:
            current_percent = int(float(percent_str))
            if current_percent != last_percent:
                speed = d.get('_speed_str', 'N/A')
                sys.stdout.write(f"\rDownloading... Progress: {current_percent}% | Speed: {speed}")
                sys.stdout.flush()
                last_percent = current_percent
        except ValueError:
            pass
    elif d['status'] == 'finished':
        print("\nDownload complete! Assembling high-definition video...")

def download_video(video_url, save_directory):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(save_directory, '%(title)s.%(ext)s'),
        'concurrent_fragment_downloads': 10,  # 10x Speed boost active
        'logger': MyQuietLogger(),
        'progress_hooks': [my_hook],
        'quiet': False,
        'no_warnings': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == '__main__':
    # Grab the URL passed by the batch file
    url_input = sys.argv[1]
    
    # --- FIXED FOR LOCAL DOWNLOADS ---
    # Get the exact directory where this python script is currently sitting
    current_folder = os.path.dirname(os.path.abspath(__file__))
    
    # Create the path for a folder named "downloads" inside it
    local_downloads = os.path.join(current_folder, 'downloads')
    
    # If the "downloads" folder doesn't exist yet, make it automatically!
    if not os.path.exists(local_downloads):
        os.makedirs(local_downloads)
    
    download_video(url_input, local_downloads)
