import speech_recognition
import time


sr = speech_recognition.Recognizer()
sr.pause_threshold = 2

def hello():
    return "Привет, чем могу помочь?"

def note():
    return "Что вы хотите записать?"


def create_note():
    def get_voice_input():
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            try:
                query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
                return query
            except speech_recognition.UnknownValueError:
                print("Не удалось распознать речь.")
    
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        print(note())
        audio = sr.listen(source=mic, timeout=2.0)  # Установили таймаут записи в 2 секунды
        try:
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            
            with open('note-list.txt', 'a', encoding='utf-8') as file:
                file.write(f'{query}\n')
                print("Задача записана, хотите просмотреть, что записали? да/нет")
                response = get_voice_input()
                if response == "да":
                    print(query)
                else:
                    print("Удачи")
        except speech_recognition.UnknownValueError:
            print("Не удалось распознать речь.")
        except speech_recognition.WaitTimeoutError:
            print("Прошло две секунды тишины. Запись завершена.")

with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
    audio = sr.listen(source=mic)
    try:
        query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        if query in ["дарова", "привет", "приветики", "ку", "здарова", "салам"]:
            print(hello())
        elif query in ["открой заметки", "заметки", "блокнот", "запись"]:
            create_note()
    except speech_recognition.UnknownValueError:
        print("Не удалось распознать речь.")
