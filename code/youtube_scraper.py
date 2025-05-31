import os
import pandas as pd
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Cargar clave API desde .env
load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")

if api_key is None:
    raise ValueError("No se encontró la clave de API en el archivo .env")

youtube = build("youtube", "v3", developerKey=api_key)

def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[-1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]
    else:
        raise ValueError("URL no válida de YouTube")

def get_comments(video_id, video_url, max_comments=500):
    comments = []
    next_page_token = None

    while len(comments) < max_comments:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            order="time",
            textFormat="plainText",
            pageToken=next_page_token
        )
        response = request.execute()
        for item in response.get("items", []):
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "video_id": video_id,
                "video_url": video_url,
                "comment_text": snippet.get("textDisplay", ""),
                "author_name": snippet.get("authorDisplayName", ""),
                "published_at": snippet.get("publishedAt", ""),
                "like_count": snippet.get("likeCount", 0)
            })
            if len(comments) >= max_comments:
                break
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break
    return comments

def main():
    urls = [
        "https://www.youtube.com/watch?v=zcdc6Nk1U_c",
        "https://www.youtube.com/watch?v=K61OTQazQwY",
        "https://www.youtube.com/watch?v=Mm9BKq9NfrI"
    ]

    all_comments = []
    for url in urls:
        try:
            video_id = get_video_id(url)
            print(f"Extrayendo comentarios del video: {video_id}")
            comments = get_comments(video_id, url)
            all_comments.extend(comments)
        except Exception as e:
            print(f"Error al procesar {url}: {e}")

    if all_comments:
        os.makedirs("data", exist_ok=True)
        df = pd.DataFrame(all_comments)
        df.to_csv("data/final_dataset.csv", index=False)
        print("Comentarios guardados en data/final_dataset.csv")
    else:
        print("No se extrajeron comentarios.")

if __name__ == "__main__":
    main()
