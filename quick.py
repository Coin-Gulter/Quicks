import os
import sys
import json
import math
import openai
import keyboard

from os import environ
from windows_toasts import InteractableWindowsToaster, ToastInputTextBox, ToastText1, ToastButton, ToastAudio

from design import quick_interface
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtTest
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = quick_interface.Ui_Quicks()
        self.ui.setupUi(self)

        self.my_path = os.getcwd()
        self.file_name = 'program_values.json'
        self.file_path = os.path.join(self.my_path, self.file_name)

        self.setWindowIcon(QIcon(os.path.join(self.my_path, 'icon36.png')))

        self.ui.button_submit.clicked.connect(self.load_values2file)

        self.values = {'key':'', 'max-token':1000}

        if not os.path.isfile(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as infile:
                json.dump(self.values, infile)

    def load_values2file(self):
        key = self.ui.linedit_enter_api.text()
        max_token = self.ui.linedit_spinbox.value()
        self.values = {'key':key, 'max-token':max_token}
        try:
            with open(self.file_path, 'w', encoding='utf-8') as infile:
                json.dump(self.values, infile)
        except:
            pass

    def show_window(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as outfile:
                self.values = json.load(outfile)
        except:
            pass
        self.ui.linedit_enter_api.setText(self.values['key'])
        self.ui.linedit_spinbox.setValue(self.values['max-token'])
        self.show()
        self.activateWindow()

class MainProgram():
    def __init__(self):
        suppress_qt_warnings()
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
        self.app = QApplication(sys.argv)

        self.main_window = MainWindow()

        self.program_wait_time = 200
        self.values = {'key':'', 'max-token':1000}

        self.work = True
        self.show_window = False
        self.show_notification = False
        self.show_input_box = False

        self.my_path = os.getcwd()
        self.file_name = 'program_values.json'
        self.file_path = os.path.join(self.my_path, self.file_name)

        self.temperature = 0.6
        self.model = "gpt-3.5-turbo"
        self.last_responce = None

        self.user_name = 'user'
        self.assistant_name = 'assistant'
        self.chat_story = [{'role':self.assistant_name, 'content':"- I'm Jastin your assistant, how can I help you ?"}]
        self.out_message = None

        self.curent_page = 0
        self.max_element_per_page = 220

        self.interactable_toast = InteractableWindowsToaster('Quicks')
        self.toast_text_notification = ToastText1()
        self.toast_text_notification.SetAudio(ToastAudio(silent=True))
        self.text4toast_notification = []
        self.toast_input_box = ToastText1()
        self.make_out_notification_text()
        self.toast_input_box.SetBody(self.out_message)
        self.toast_input_box.AddInput(ToastInputTextBox('question'))
        self.toast_input_box.AddAction(ToastButton('Submit', 'submit'))
        self.toast_input_box.SetAudio(ToastAudio(silent=True))
        self.toast_input_box.on_activated = self.answear2question

        keyboard.add_hotkey('ctrl+alt+s', self.close_program)
        keyboard.add_hotkey('ctrl+alt+d', self.show_main_window)
        keyboard.add_hotkey('ctrl+alt+f', self.show_ask_box)
        keyboard.add_hotkey('ctrl+alt+g', self.show_last_responce)
        keyboard.add_hotkey('ctrl+alt+right', self.next_page)
        keyboard.add_hotkey('ctrl+alt+left', self.previous_page)

    def main_program_start(self):
        self.set_notification('"Quicks" is working now')
        while self.work:
            if self.show_window:
                self.show_window = False
                self.main_window.show_window()
            elif self.show_notification:
                if self.show_input_box:
                    self.interactable_toast.show_toast(self.toast_input_box)
                    self.show_input_box = False
                else:
                    self.toast_text_notification.SetBody(self.text4toast_notification[self.curent_page])
                    self.interactable_toast.show_toast(self.toast_text_notification)
                
                self.show_notification = False   

            QtTest.QTest.qWait(self.program_wait_time)

        self.toast_text_notification.SetBody(self.text4toast_notification[self.curent_page])
        self.interactable_toast.show_toast(self.toast_text_notification)


    def answear2question(self, activatedEventArgs):
        input_question = '- ' + activatedEventArgs.inputs['question']
        self.chat_story.append({'role':self.user_name, 'content':input_question})

        try:
            with open(self.file_path, 'r', encoding='utf-8') as outfile:
                self.values = json.load(outfile)
        except:
            pass

        try:
            openai.api_key = self.values['key']
            self.last_responce = openai.ChatCompletion.create(model=self.model, messages=self.chat_story, temperature=self.temperature, max_tokens=self.values['max-token'])
            print(self.last_responce)
            self.chat_story.append({'role': self.assistant_name, 'content': '- ' + self.last_responce['choices'][0]['message']['content']})
            print(self.chat_story)
        except:
            self.chat_story.append({'role': self.assistant_name, 'content': "- Something went wrong while asking.\n Check if you have ethernet connection\nor if your api key is right."})

        self.make_out_notification_text()
        self.set_notification(self.out_message)

        self.chat_story.pop(0)
        self.chat_story.pop(0)

    def previous_page(self):
        if self.curent_page > 0:
            self.curent_page -= 1
        self.show_notification = True

    def next_page(self):
        if self.curent_page < (len(self.text4toast_notification)-1):
            self.curent_page += 1
        self.show_notification = True

    def show_last_responce(self):
        self.set_notification(self.out_message)

    def make_out_notification_text(self):
        self.out_message = ''
        line = self.chat_story[-1]
        self.out_message += line['role'] + '\t' + line['content'] + '\n'

    def show_main_window(self):
        self.show_window = True

    def set_notification(self, text):
        if type(text) is str:

            self.text4toast_notification = []
            self.curent_page = 0
            text = text.replace('\n', '  ')
            all_pages = math.ceil(len(text)/self.max_element_per_page)
            page_index = 0

            while len(text)>self.max_element_per_page:
                page_index += 1
                text = f'{page_index}/{all_pages}\n' + text
                self.text4toast_notification.append(text[:self.max_element_per_page])
                text = text[self.max_element_per_page:]

            self.text4toast_notification.append(text)
            print(self.text4toast_notification)

        else:
            self.text4toast_notification = 'There is no information :('
        self.show_notification = True


    def show_ask_box(self):
        self.make_out_notification_text()
        self.toast_input_box.SetBody(self.out_message)
        self.show_notification = True
        self.show_input_box = True

    def close_program(self):
        self.set_notification('"Quicks" is closed')
        self.work = False

if __name__ == "__main__":

    my_program = MainProgram()
    my_program.main_program_start()
