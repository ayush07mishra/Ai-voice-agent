# voice/stt.py

import speech_recognition as sr


def listen():
    r = sr.Recognizer()
    
    # Configure parameters for instant listening
    r.dynamic_energy_threshold = True
    r.energy_threshold = 300  # Reasonable default for typical microphones
    r.pause_threshold = 0.8   # Time to wait before ending phrase

    try:
        # Use the default system microphone
        with sr.Microphone() as source:
            print("\nListening... Speak now...")

            # Capture the audio from the microphone without slow ambient noise calibration
            # to prevent cutting off the first words of the user
            audio = r.listen(source, timeout=8, phrase_time_limit=10)
            print("Processing voice input...")

            # Use Google Speech Recognition for Hindi (hi-IN)
            # This handles Hinglish and English as well
            text = r.recognize_google(audio, language="hi-IN")
            print(f"Customer (Voice): {text}")
            return text

    except sr.WaitTimeoutError:
        print("No speech detected (timeout).")
        return ""
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request speech recognition results; {e}")
        return ""
    except Exception as e:
        print(f"Error capturing audio: {e}")
        return ""
