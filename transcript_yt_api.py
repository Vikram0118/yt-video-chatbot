import googleapiclient.discovery

def get_youtube_transcript(api_key, video_id):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    try:
        # Get video details
        video_response = youtube.videos().list(part="snippet", id=video_id).execute()
        video_title = video_response['items'][0]['snippet']['title']

        # Get transcript
        transcript_response = youtube.captions().list(
            part="snippet",
            videoId=video_id
        ).execute()

        captions = transcript_response.get("items", [])

        # Extract transcript text
        transcript = ""
        for caption in captions:
            transcript += caption["snippet"]["text"] + " "

        return {
            "video_title": video_title,
            "transcript": transcript.strip()
        }

    except googleapiclient.errors.HttpError as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Replace 'YOUR_YOUTUBE_API_KEY' with your actual YouTube API key
    api_key = 'AIzaSyCZ_Voq3x13rC3JgQZSHnw9EgCYn-htcb0'

    # Replace 'VIDEO_ID' with the actual YouTube video ID
    video_id = 'JL4OoKJyNrc'

    transcript_data = get_youtube_transcript(api_key, video_id)

    if transcript_data:
        print(transcript_data)
        # print(f"Video Title: {transcript_data['video_title']}")
        # print(f"Transcript:\n{transcript_data['transcript']}")