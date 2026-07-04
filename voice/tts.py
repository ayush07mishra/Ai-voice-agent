# voice/tts.py

import os
import subprocess
import winsound
from gtts import gTTS

# PIPER_PATH = r"C:\piper\piper.exe"
# MODEL = r"C:\piper\hi_IN-voice.onnx"
PIPER_PATH = r"C:\piper\piper.exe"
MODEL = r"C:\piper\en_US-lessac-medium.onnx"


def speak(text):
    # Clean up previous audio files to avoid stale playback
    for f in ["voice.wav", "voice.mp3"]:
        if os.path.exists(f):
            try:
                os.remove(f)
            except Exception:
                pass

    # Method 1: Piper (Local TTS)
    if os.path.exists(PIPER_PATH) and os.path.exists(MODEL):
        output_file = "voice.wav"
        subprocess.run(
            [
                PIPER_PATH,
                "-m",
                MODEL,
                "-f",
                output_file
            ],
            input=text.encode("utf-8")
        )
        try:
            winsound.PlaySound(output_file, winsound.SND_FILENAME)
        except Exception:
            pass
        return

    # Method 2: gTTS (Google Cloud TTS)
    try:
        tts = gTTS(text=text, lang='hi')
        tts.save("voice.mp3")
    except Exception as e:
        print(f"\n[TTS Error] Could not generate fallback speech: {e}")
