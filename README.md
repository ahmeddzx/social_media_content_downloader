# 📥 Social Media Content Downloader

Bulk-download videos, images, captions, and metadata from popular platforms  
(**TikTok, Instagram, X/Twitter, YouTube, Facebook, and more**) using [`yt-dlp`](https://github.com/yt-dlp/yt-dlp).

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen.svg)

---

## ✨ Features
- ✅ Download from a single URL or batch via `.txt` file.  
- ✅ Saves **best-quality media**, thumbnails, subtitles (if available), and JSON metadata.  
- ✅ Auto-organizes outputs by platform/channel.  
- ✅ Handles retries and rate limits gracefully.  

---

## 🚀 Quick Start

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
pip install -r requirements.txt

python main.py --url "https://www.tiktok.com/@someuser/video/123..."

python main.py --file urls.txt

downloads/

social_media_content_downloader/
│── main.py               # Main script
│── requirements.txt      # Python dependencies
│── urls.txt              # Example input file (list of URLs)
└── downloads/            # Output folder for media, captions, metadata
