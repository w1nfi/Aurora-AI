import random
import speech_recognition as sr
import sys

sr_obj = sr.Recognizer()
sr_obj.pause_threshold = 0.5

commands_dict = {
    'greeting': ['привет', 'приветствую', 'дарова'],
    'create_task': ['добавить задачу', 'создать задачу', 'заметка'],
    'exit': ['выход', 'закрыть', 'пока']
}

def listen_command():
    try:
        with sr.Microphone() as source:
            sr_obj.adjust_for_ambient_noise(source=source, duration=0.5)
            audio = sr_obj.listen(source=source)
            query = sr_obj.recognize_google(audio, language='ru-RU').lower()

        return query
    except sr.UnknownValueError:
        return 'Damn... Не понял что ты сказал :/'

def greeting():
    return 'Привет, чем могу помочь!'

def create_task():
    print('Что добавим в список дел?')
    query = listen_command()

    with open('todo-list.txt', 'a', encoding='utf-8') as file:
        file.write(f'❗️ {query}\n')

    return f'Задача {query} добавлена в todo-list!'

def exit_program():
    print('До свидания!')
    sys.exit()

def main():
    query = listen_command()

    for command, keywords in commands_dict.items():
        if query in keywords:
            if command == 'exit':
                exit_program()
            else:
                print(globals()[command]())

if __name__ == '__main__':
    main()
