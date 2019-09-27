print('D.E.I.Z.A.N.O.')
import speech_recognition as sr
from pathlib import Path
r = sr.Recognizer()
harvard = sr.WavFile("TestAudio/harvard.wav")
with harvard as source:
    audio = r.record(source)
try:
    print("Transcription: " + r.recognize_google(audio))   # recognize speech using Google Speech Recognition
except LookupError:                                 # speech is unintelligible
    print("Could not understand audio")