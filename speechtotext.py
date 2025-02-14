import subprocess

def extract_audio(video_path, audio_path):
    """Extracts audio from video using FFmpeg."""
    try:
        command = ["ffmpeg", "-i", video_path, "-q:a", "0", "-map", "a", audio_path, "-y"]
        subprocess.run(command, check=True)
        print(f"✅ Audio extracted successfully: {audio_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ FFmpeg error: {e}")

# Test the function
video_path = "input_video.mp4"  # Replace with your actual video file
audio_path = "output_audio.mp3"
extract_audio(video_path, audio_path)
