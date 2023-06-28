import random
import speech_recognition as sr
import sys
import subprocess

import pyautogui


sr_obj = sr.Recognizer()
sr_obj.pause_threshold = 0.5

commands_dict = {
    'greeting': ['привет', 'приветствую', 'дарова'],
    'create_task': ['добавить задачу', 'создать задачу', 'заметка'],
    'open_browser': ['открой браузер', 'открыть браузер'],
    'open_google': ['открой гугл', 'открыть гугл'],
    'exit': ['выход', 'закрыть', 'пока'],
    'hide_windows': ['скрой окна', 'скрой все окна', 'скрой все'],
    'play_phonk': ['включи фонк', 'воспроизведи фонк','вруби фонк'],
}

def listen_command():
    try:
        with sr.Microphone() as source:
            sr_obj.adjust_for_ambient_noise(source=source, duration=0.5)
            audio = sr_obj.listen(source=source)
            query = sr_obj.recognize_google(audio, language='ru-RU').lower()

        return query
    except sr.UnknownValueError:
        return 'Вытяни хуй изо рта и потом скажи'

def greeting():
    return 'Привет, чем могу помочь!'

def create_task():
    print('Что добавим в список дел?')
    query = listen_command()

    with open('todo-list.txt', 'a', encoding='utf-8') as file:
        file.write(f'❗️ {query}\n')

    return f'Задача {query} добавлена в todo-list!'

def open_google():
    subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe')

def open_browser():
    subprocess.Popen(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')

def hide_windows():
    pyautogui.hotkey('win', 'd')

def play_phonk():
    music_directory = r'C:\Users\lomba\Desktop\Spotify\SpotiFlyer\Playlists\God_'
    subprocess.Popen(r'explorer.exe ' + music_directory)

def exit_program():
    print('До свидания!')
    sys.exit()

def main():
    query = listen_command()

    for command, keywords in commands_dict.items():
        if query in keywords:
            print(f"Recognized command: {command}")
            if command == 'exit':
                exit_program()
            else:
                print(f"Executing command: {command}")
                print(globals()[command]())



if __name__ == '__main__':
    main()
