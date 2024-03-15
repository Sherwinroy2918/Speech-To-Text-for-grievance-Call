import logging
import speech_recognition as sr
from googletrans import Translator
from langdetect import detect
import threading
import time
import keyboard  


def detect_and_translate(audio_data):
    """Detects language and translates audio to English if it's in Hindi or a mix of Hindi and English."""
    try:
        recognizer = sr.Recognizer()
        transcript = recognizer.recognize_google(audio_data, language="hi-IN", show_all=True)  # Recognize speech in Hindi
        if transcript:
            transcript = transcript['alternative'][0]['transcript']
            detected_language = detect(transcript)
            if detected_language in ['hi', 'mr']:  # Hindi or Marathi detected
                translator = Translator()
                translated_text = translator.translate(transcript, src=detected_language, dest='en').text
                return translated_text
            else:
                return transcript  # Return transcript as it is (already in English)
        else:
            return None
    except sr.UnknownValueError:
        logging.warning("Speech recognition could not understand audio.")
        return None
    except sr.RequestError as e:
        logging.error(f"Could not request results from Google Speech-to-Text service: {e}")
        return None

def listen_keyboard():
    while True:
        if keyboard.is_pressed('esc'):
            print("Program terminated.")
            break
        time.sleep(0.1)  # Sleep for a short time to avoid high CPU usage

def main():
    logging.basicConfig(level=logging.INFO)
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Start a thread for listening to keyboard events
    keyboard_thread = threading.Thread(target=listen_keyboard, daemon=True)
    keyboard_thread.start()

    while True:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Speak something...")

            try:
                audio_data = recognizer.listen(source, timeout=5)  # Listen for 5 seconds
                print("Listening...")

                text = detect_and_translate(audio_data)
                if text:
                    print("Transcription:", text)

            except sr.WaitTimeoutError:
                print("Timeout: No speech detected.")
                continue

if __name__ == "__main__":
    main()
