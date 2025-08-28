
import os
import argparse
from datetime import datetime
from tqdm import tqdm

try:
    import yt_dlp as ytdlp
except Exception as e:
    raise SystemExit("yt-dlp is required. Install with: pip install yt-dlp") from e

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")

def download_one(url: str):
    os.makedirs(OUT_DIR, exist_ok=True)
    ydl_opts = {
        "outtmpl": os.path.join(OUT_DIR, "%(extractor_key)s/%(uploader)s/%(upload_date>%Y-%m-%d)s_%(title).100B_%(id)s.%(ext)s"),
        "writeinfojson": True,
        "writedescription": True,
        "writesubtitles": True,
        "writeautomaticsub": True,
        "writethumbnail": True,
        "consoletitle": True,
        "noprogress": True,
        "ignoreerrors": True,
        "retries": 5,
        "fragment_retries": 10,
        "continuedl": True,
        "merge_output_format": "mp4",
        "postprocessors": [
            {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"},
            {"key": "FFmpegMetadata"},
            {"key": "EmbedThumbnail"},
        ],
    }
    with ytdlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def read_urls_from_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]

def main():
    parser = argparse.ArgumentParser(description="Social Media Content Downloader (yt-dlp)")
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--url", help="Single URL to download")
    g.add_argument("--file", help="Path to a text file with URLs (one per line)")
    args = parser.parse_args()

    urls = [args.url] if args.url else read_urls_from_file(args.file)
    for u in tqdm(urls, desc="Downloading", unit="item"):
        try:
            download_one(u)
        except Exception as e:
            print(f"Failed: {u} -> {e}")

if __name__ == "__main__":
    main()
