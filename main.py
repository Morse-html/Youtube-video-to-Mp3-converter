import os
import sys
import yt_dlp

def download_youtube_as_mp3(video_url: str, output_path: str = ".") -> None:
    """
    Downloads audio from YouTube and converts it to MP3 using Firefox cookies.
    """
    os.makedirs(output_path, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': True,

        # Pull cookies directly from Firefox
        'cookiesfrombrowser': ('firefox',),
    }

    try:
        print(f"Starting download for: {video_url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download and conversion complete!")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    url = input("Enter YouTube video URL: ").strip()
    if url:
        download_youtube_as_mp3(url)
    else:
        print("No URL provided.")
