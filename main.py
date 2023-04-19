import win32com.client as wincom

if __name__ == '__main__':
    print("Welcome to the RoboSpeaker 1.1. Created by Arsal")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q":
            TextToSpeech.speak("Bye bye friend")
            break
        TextToSpeech = wincom.Dispatch("sapi.SpVoice")
        TextToSpeech.speak(x)

    # OTHER METHOD TO SPEAK ----->
        # text_speech = pyttsx3.init()
        # text_speech.say(x)
        # text_speech.runAndWait()
