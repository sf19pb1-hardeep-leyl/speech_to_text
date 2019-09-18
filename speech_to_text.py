# pip3 install SpeechRecognition
# pip3 install PyAudio

import speech_recognition as sr

r = sr.Recongnizer()
with sr.Microphone() as source:
    print("Say something")
    audio = r.listen(source)
    print("Time over, thanks")

print("TEXT: "+r.recognize_google_audio))
