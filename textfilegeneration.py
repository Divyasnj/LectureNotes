import whisper

def transcribe_audio(audio_path, text_output_path):
    """Transcribes speech from an audio file and saves it to a text file."""
    try:
        model = whisper.load_model("small")  # You can use "tiny", "base", "small", "medium", or "large"
        result = model.transcribe(audio_path)

        # Save the transcribed text to a file
        with open(text_output_path, "w", encoding="utf-8") as file:
            file.write(result["text"])

        print(f"✅ Transcription completed! Text saved to: {text_output_path}")
    except Exception as e:
        print(f"❌ Error transcribing audio: {e}")

# Run transcription
audio_path = "output_audio.mp3"  # Path to your extracted audio file
text_output_path = "transcription.txt"
transcribe_audio(audio_path, text_output_path)
