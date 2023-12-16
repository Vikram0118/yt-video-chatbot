from youtube_transcript_api import YouTubeTranscriptApi

def get_video_transcript(video_url):
    try:
        video_id = video_url.split("v=")[1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except IndexError:
        print("Error: Video ID not found in the URL.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":

    video_url = 'https://www.youtube.com/watch?v=JL4OoKJyNrc'

    transcript_data = get_video_transcript(video_url)

    if transcript_data:
        print(transcript_data)
        # for entry in transcript_data:
            # print(f"{entry['start']} - {entry['start'] + entry['duration']}: {entry['text']}")
