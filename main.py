import subprocess
import whisper

def extract_audio(video_path, audio_path):
    """Extracts audio from video using FFmpeg."""
    try:
        command = ["ffmpeg", "-i", video_path, "-q:a", "0", "-map", "a", audio_path, "-y"]
        subprocess.run(command, check=True)
        print(f"✅ Audio extracted successfully: {audio_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ FFmpeg error: {e}")

def transcribe_audio(audio_path, text_output_path):
    """Transcribes speech from an audio file and saves it to a text file."""
    try:
        model = whisper.load_model("small")  # Options: "tiny", "base", "small", "medium", "large"
        result = model.transcribe(audio_path)

        # Save transcription to a file
        with open(text_output_path, "w", encoding="utf-8") as file:
            file.write(result["text"])

        print(f"✅ Transcription completed! Text saved to: {text_output_path}")
    except Exception as e:
        print(f"❌ Error transcribing audio: {e}")

# File paths (replace with your actual file paths)
video_path = "input_video.mp4"  # Your video file
audio_path = "output_audio.mp3"  # Extracted audio file
text_output_path = "transcription.txt"  # Final transcript file

# Run the pipeline
extract_audio(video_path, audio_path)
transcribe_audio(audio_path, text_output_path)
