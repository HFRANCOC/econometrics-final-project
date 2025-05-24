import os
import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Inicializar cliente de YouTube
youtube = build(
    serviceName="youtube",
    version="v3",
    developerKey=API_KEY
)


def get_video_title(video_id):
    response = youtube.videos().list(
        part="snippet",
        id=video_id
    ).execute()

    items = response.get("items", [])
    if items:
        return items[0]["snippet"]["title"]
    return "Unknown Title"


def get_comments(video_id, max_comments=500):
    comments = []

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    )

    while request and len(comments) < max_comments:
        response = request.execute()

        for item in response["items"]:
            top_comment = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "comment_id": item["id"],
                "text": top_comment["textDisplay"],
                "video_id": video_id,
                "video_title": get_video_title(video_id)
            })

        request = youtube.commentThreads().list_next(request, response)

    return comments[:max_comments]


def save_to_csv(comments, filename="data/dataset.csv"):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(base_dir, filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    df = pd.DataFrame(comments)
    df.to_csv(filepath, index=False)
    print(f"Guardado en {filepath} con {len(df)} comentarios.")


def main():
    video_id = "9FcaUhySrbA"
    video_title = get_video_title(video_id)
    print(f"Extrayendo comentarios de: {video_title} (ID: {video_id})")

    comments = get_comments(video_id)
    save_to_csv(comments)


if __name__ == "__main__":
    main()