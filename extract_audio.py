from moviepy import VideoFileClip
import os

def extract_audio(video_path, output_audio_path):
    """
    Extracts audio from a video file and saves it as a WAV file.
    """

    # Load the video file
    video = VideoFileClip(video_path)

    # Extract the audio
    audio = video.audio

    # Write the audio to a WAV file
    audio.write_audiofile(output_audio_path)

    # Close the video file
    video.close()

    print(f"Audio extracted successfully and saved to: {output_audio_path}")


if __name__ == "__main__":
    # Example test file
    video_file = "sample_video.mp4"
    audio_file = "output_audio.wav"

    if not os.path.exists(video_file):
        print("Please place a video file named 'sample_video.mp4' in this folder.")
    else:
        extract_audio(video_file, audio_file)