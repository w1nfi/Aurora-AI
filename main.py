import speech_recognition

sr = speech_recognition.Recognizer()

sr.pause_threshold = 1

def hello():
    return "Привет, чем могу помочь?"

with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
    audio = sr.listen(source=mic)
    try:
        query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        if query in ["дарова","привет","приветики","ку","здарова","салам"]:
            print(hello())
       
    except speech_recognition.UnknownValueError:
        print("Не удалось распознать речь.")
