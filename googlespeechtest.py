import speech_recognition as sr

filename ="asano.wav"
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio = r.record(source)
try:
    text = "Google Speech Recognition thinks you said " + r.recognize_google(audio, language='ja-JP')
    print(text)
except:
    pass
