from pytube import YouTube
from moviepy.editor import *
from pydub import AudioSegment
import os

def download_youtube_audio(youtube_url, output_path):
    # Download YouTube video
    yt = YouTube(youtube_url)
    video = yt.streams.filter(only_audio=True).first()
    video.download(output_path=output_path, filename='temp')

    # Convert to audio using moviepy
    video_path = os.path.join(output_path, 'temp.mp4')
    audio = AudioFileClip(video_path)
    audio_path = os.path.join(output_path, 'temp_audio.wav')
    audio.write_audiofile(audio_path)

    # Convert to MP3 using pydub
    wav_audio = AudioSegment.from_wav(audio_path)
    mp3_audio = wav_audio.export(os.path.join(output_path, 'output.mp3'), format="mp3")

    # Clean up temporary files
    os.remove(video_path)
    os.remove(audio_path)

    print("Audio converted to MP3 successfully!")
