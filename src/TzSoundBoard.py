import os
import pygame
import mutagen # added for playback length etc. possible slider to indicate play position.

try:
    # python 3
    import tkinter
    from tkinter import filedialog
except ImportError:
    # python 2
    import Tkinter as tkinter


class TzSoundBoard(object):

    def __init__(self):
        self.column = 0
        self.row = 0
        self.menu = None
        pygame.mixer.init()
        self.main_window = tkinter.Tk()
        self.main_window.geometry("500x300+150+150")
        self.main_window.title('TzSoundBoard')
        self.add_button(self.main_window, "Crash", "Crash.mp3")
        self.add_button(self.main_window, "Dog Snarling", "Dog_Snarling.mp3")
        self.volume_controls()
        self.create_menu()
        self.main_window.mainloop()

    def client_exit(self):
        pygame.mixer.music.stop()
        self.main_window.destroy()

    def pick_file(self):
        file_name = filedialog.askopenfilename(initialdir='./', title="Select file", filetypes=(("mp3 files", "*.mp3"), ("wav files", "*.wav"), ("ogg files", "*.ogg")))
        self.add_button(self.main_window, os.path.basename(file_name), file_name)

    def create_menu(self):
        self.menu = tkinter.Menu(self.main_window)
        self.main_window.config(menu=self.menu)

        file = tkinter.Menu(self.menu)
        file.add_command(label="Add Sound Effect", command=self.pick_file)
        file.add_command(label="Exit", command=self.client_exit)

        self.menu.add_cascade(label="File", menu=file)

    def set_volume(self, value):
        value = int(value)
        print("is called: {}".format(value))
        if value == 0:
            pygame.mixer.music.set_volume(0)
        else:
            pygame.mixer.music.set_volume(value/100)

    def volume_controls(self):
        tkinter.Scale(self.main_window, label="Volume", orient=tkinter.HORIZONTAL, from_=0, to=100, command=self.set_volume).grid(row=2, column=0)

    def play_music(self, file_to_play):
        pygame.mixer.music.load(file_to_play)
        pygame.mixer.music.play()

    def add_button(self, window, text, file_to_play):
        self.column += 1
        return tkinter.Button(window, text=text, height=10, width=20, command=lambda: self.play_music(file_to_play)).grid(row=self.row, column=self.column)

my = TzSoundBoard()


class Sound(object):
    pass