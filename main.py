import random
import speech_recognition as sr
import sys
import subprocess
import pyautogui
import asyncio
import threading

class VoiceAssistant:
    def __init__(self):
        self.sr_obj = sr.Recognizer()
        self.sr_obj.pause_threshold = 0.5

        self.commands_dict = {
            'greeting': ['привет', 'приветствую', 'дарова'],
            'create_task': ['добавить задачу', 'создать задачу', 'заметка'],
            'open_browser': ['открой браузер', 'открыть браузер'],
            'open_google': ['открой гугл', 'открыть гугл'],
            'exit': ['выход', 'закрыть', 'пока'],
            'hide_windows': ['скрой окна', 'скрой все окна', 'скрой все'],
            'play_phonk': ['включи фонк', 'воспроизведи фонк','вруби фонк'],
        }

    def listen_command(self):
        try:
            with sr.Microphone() as source:
                self.sr_obj.adjust_for_ambient_noise(source=source, duration=0.5)
                audio = self.sr_obj.listen(source=source)
                query = self.sr_obj.recognize_google(audio, language='ru-RU').lower()

            return query
        except sr.UnknownValueError:
            return 'Вытяни хуй изо рта и потом скажи'

    def greeting(self):
        return 'Привет, чем могу помочь!'

    def create_task(self):
        print('Что добавим в список дел?')
        query = self.listen_command()

        with open('todo-list.txt', 'a', encoding='utf-8') as file:
            file.write(f'❗️ {query}\n')

        return f'Задача {query} добавлена в todo-list!'

    def open_google(self):
        subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe')

    def open_browser(self):
        subprocess.Popen(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')

    def hide_windows(self):
        pyautogui.hotkey('win', 'd')

    def play_phonk(self):
        music_directory = r'C:\Users\lomba\Desktop\Spotify\SpotiFlyer\Playlists\God_'
        subprocess.Popen(r'explorer.exe ' + music_directory)

    def exit_program(self):
        print('До свидания!')
        sys.exit()

    def handle_command(self, command):
        if command == 'greeting':
            return self.greeting()
        elif command == 'create_task':
            return self.create_task()
        elif command == 'open_google':
            self.open_google()
        elif command == 'open_browser':
            self.open_browser()
        elif command == 'hide_windows':
            self.hide_windows()
        elif command == 'play_phonk':
            self.play_phonk()
        elif command == 'exit':
            self.exit_program()
        else:
            return 'Команда не распознана.'

    def run(self):
        while True:
            query = self.listen_command()

            for command, keywords in self.commands_dict.items():
                if query in keywords:
                    print(f"Recognized command: {command}")
                    response = self.handle_command(command)
                    if response:
                        print(response)
                    break

if __name__ == '__main__':
    assistant = VoiceAssistant()
    threading.Thread(target=assistant.run).start()
