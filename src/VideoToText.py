import sys
import os
from pytube import YouTube
import whisper
from transformers import pipeline
from nltk.tokenize import sent_tokenize

ASSET_PATH = './assets'


def ensure_directories_exist():
    """Ensures that the required directories exist."""
    os.makedirs(f"{ASSET_PATH}/audio", exist_ok=True)
    os.makedirs(f"{ASSET_PATH}/transcripts", exist_ok=True)
    os.makedirs(f"{ASSET_PATH}/summaries", exist_ok=True)


def download_video(video_link, audio_mp4_folder=f"{ASSET_PATH}/audio"):
    """Downloads the video from YouTube in the highest resolution."""
    yt = YouTube(video_link)
    video_title = yt.title
    initials = ''.join(word[0].upper() for word in video_title.split())
    audio_mp4_filename = f"{initials}.mp4"
    audio_mp4_path = os.path.join(audio_mp4_folder, audio_mp4_filename)  # Use os.path.join for path construction
    print(f"Downloading {video_title}...")
    yt.streams.get_highest_resolution().download(output_path=audio_mp4_folder, filename=audio_mp4_filename)
    print("Download complete.")
    return audio_mp4_path, initials

def transcribe_audio(audio_path, initials):
    """Transcribes the audio from the given path using Whisper and saves the transcript."""
    print("Loading Whisper model...")
    model = whisper.load_model("base")
    print("Transcribing audio...")
    result = model.transcribe(audio_path)
    transcript_path = f"{ASSET_PATH}/transcripts/{initials}_transcript.txt"
    with open(transcript_path, 'w') as file:
        file.write(result['text'])
    print("Transcription and saving complete.")
    return transcript_path

def summarize_text(transcript_path, initials):
    """Generates a summary of the transcribed text and saves it."""
    # Placeholder for summarization logic
    # In practice, replace this with actual summarization logic, possibly using NLP libraries or APIs.
    summary_path = f"{ASSET_PATH}/summaries/{initials}_summary.txt"
    with open(transcript_path, 'r') as file:
        text = file.read()

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    text_arr = text.split(" ")
    summary_text = summarizer(text, min_length=len(text_arr) // 3, max_length=2048, do_sample=True)

    with open(summary_path, 'w') as file:
        file.write(summary_text[0]['summary_text'])
    print("Summary generated and saved.")

def main(video_link):
    ensure_directories_exist()  # Ensure required directories exist
    
    try:
        audio_mp4_path, initials = download_video(video_link)
        transcript_path = transcribe_audio(audio_mp4_path, initials)
        summarize_text(transcript_path, initials)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <YouTube Link>")
    else:
        print("Starting script...")
        main(sys.argv[1])
        print("Script finished.")
