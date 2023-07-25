from googleapiclient.discovery import build

API_KEY = "AIzaSyARAZ4QqMqrIgxaeEifm5qVBkBb8SuYgIw"  # API-key
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)


def get_video_data(video_id):
    request = youtube.videos().list(part="snippet,statistics", id=video_id)
    response = request.execute()

    if 'items' in response and len(response['items']) > 0:
        return response['items'][0]
    return None

# Test


if __name__ == "__main__":
    video_id = "A_SAMPLE_VIDEO_ID"
    data = get_video_data(video_id)
    print(data)
