import speech_recognition as sr

# Function to recognize speech input
def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Say the keyword to unlock:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        spoken_text = recognizer.recognize_google(audio).lower()
        return spoken_text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

# Main function to lock and unlock the resume
def lock_resume():
    locked = True
    while True:
        if locked:
            spoken_text = recognize_speech()
            if "open sesame" in spoken_text:  # Change "open sesame" to your chosen keyword/phrase
                print("Resume unlocked. You have access.")
                locked = False
            else:
                print("Access denied. Try again.")
        else:
            print("Resume is unlocked. You have access.")
            break

# Call the main function to lock and unlock the resume
lock_resume()